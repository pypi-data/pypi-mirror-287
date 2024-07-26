#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2023-2024 Robin Jarry

"""
Convert linux networking configuration to a DOT graph. The output can be piped
to dot to convert it to SVG or other formats. Example:

    %(prog)s | dot -Tsvg > net.svg

System dependencies: iproute2, ethtool
"""

import argparse
import json
import os
import re
import subprocess
import sys

from . import bits


def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "-2",
        "--l2-addresses",
        action="store_true",
        help="""
        Display mac addresses.
        """,
    )
    parser.add_argument(
        "-4",
        "--ipv4-addresses",
        action="store_true",
        help="""
        Display IPv4 addresses.
        """,
    )
    parser.add_argument(
        "-6",
        "--ipv6-addresses",
        action="store_true",
        help="""
        Display IPv6 addresses.
        """,
    )
    parser.add_argument(
        "-l",
        "--local",
        action="store_true",
        help="""
        Display loopback interfaces and local addresses.
        """,
    )
    args = parser.parse_args()

    namespaces = preprocess(get_running(), args)

    print("graph {")
    print("  node [fontsize=11 fontname=monospace margin=0];")
    print("  edge [fontsize=11 fontname=monospace margin=0];")
    print("  graph [fontsize=11 fontname=monospace compound=true style=dotted];")

    for ns, links in namespaces.items():
        print()
        if ns:
            print(f"  subgraph {safe(ns)} {{")
            print(f'    label="{ns}";')
            print("    cluster=true;")
            print()
            indent = "  "
        else:
            indent = ""
        for link in links:
            print(f"{indent}  {link['id']} [{node_attrs(link)}];")
        if ns:
            print("  }")

    print()
    master_edges = []
    link_edges = []
    for links in namespaces.values():
        for link in links:
            if "master" in link:
                edge = (link["id"], link["master"], link.get("vlans", []))
                reverse = (edge[1], edge[0], edge[2])
                if reverse in master_edges:
                    master_edges.remove(reverse)
                master_edges.append(edge)
            if "link" in link:
                edge = (link["id"], link["link"])
                reverse = (edge[1], edge[0])
                if reverse in link_edges:
                    link_edges.remove(reverse)
                link_edges.append(edge)
    for a, b, vlans in master_edges:
        if vlans:
            print(f'  {a} -- {b} [label="VLAN\\n{bits.bit_list(vlans)}"];')
        else:
            print(f"  {a} -- {b};")
    for a, b in link_edges:
        print(f"  {a} -- {b} [style=dashed];")

    print()
    print("  {")
    print("    rank=sink cluster=false;")
    for link in namespaces[""]:
        if "master" not in link and "link" not in link:
            print(f"    {link['id']};")
    print("  }")

    print("}")


def safe(n):
    return re.sub(r"\W", "_", n)


COLORS = {
    "bond": "deeppink",
    "bridge": "red",
    "loopback": "peru",
    "veth": "blue",
    "vlan": "green",
    "vxlan": "darkgreen",
}
SHAPES = {
    "bond": "house",
    "bridge": "octagon",
    "loopback": "invtriangle",
    "vlan": "rectangle",
    "vxlan": "rectangle",
}


def node_attrs(link):
    attrs = {}
    color = COLORS.get(link["kind"], "gray")
    attrs["tooltip"] = '"' + "\\n".join(link["tip"]) + '"'
    attrs["color"] = color
    attrs["shape"] = SHAPES.get(link["kind"], "oval")
    if attrs["shape"] == "rectangle":
        attrs.setdefault("margin", "0.05")
    labels = [
        f"<b>{link['name']}</b>",
    ]
    if "alias" in link:
        alias = link["alias"]
        if len(alias) > 16:
            alias = alias[:15] + "…"
        labels.append(f'<font color="slategray"><i>&quot;{alias}&quot;</i></font>')
    labels += (
        [
            f'<font color="{color}">{link["kind"]}</font>',
        ]
        + [
            f'<font color="{color}">{key} {value}</font>'
            for key, value in link["attributes"].items()
        ]
        + [f'<font color="orange">{mac}</font>' for mac in link["l2"]]
        + [f'<font color="purple">{v4}</font>' for v4 in link["ipv4"]]
        + [f'<font color="purple">{v6}</font>' for v6 in link["ipv6"]]
    )
    attrs["label"] = f"<{'<br/>'.join(labels)}>"
    return " ".join(f"{k}={v}" for k, v in attrs.items())


def iproute2_cmd(prog, ns, *cmd):
    args = [prog, "-d", "-j"]
    if ns:
        args.extend(["-n", ns])
    args.extend(cmd)
    out = subprocess.check_output(args).decode("utf-8")
    if not out.strip():
        return []
    return json.loads(out)


def ip(ns, *cmd):
    return iproute2_cmd("ip", ns, *cmd)


def bridge(ns, *cmd):
    return iproute2_cmd("bridge", ns, *cmd)


def get_nsids(netns):
    try:
        missing_nsid = set(os.listdir("/run/netns"))
    except OSError:
        missing_nsid = set()
    nsids = {}
    for ns in ip(netns, "netns", "list-id"):
        nsid = ns["nsid"]
        if "name" in ns:
            missing_nsid.discard(ns["name"])
            nsids[nsid] = ns["name"]
        elif nsid == 0:
            # XXX: hack: there is absolutely no guarantee that 0 is a special
            # number that will always point to the netns of PID 1. However,
            # this workaround seems to work most of the time.
            nsids[nsid] = ""
    for name in missing_nsid:
        cmd = ["ip"]
        if netns != "":
            cmd += ["-n", netns]
        subprocess.call(
            cmd + ["netns", "set", name, "auto"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

    if missing_nsid:
        for ns in ip(netns, "netns", "list-id"):
            nsid = ns["nsid"]
            if nsid not in nsids and "name" in ns:
                nsids[nsid] = ns["name"]

    return nsids


def get_running():
    addrs = ip("", "addr", "show")
    running = {
        "": {
            "addr_names": {a["ifname"]: a for a in addrs},
            "addr_ids": {a["ifindex"]: a for a in addrs},
            "nsids": get_nsids(""),
        },
    }
    for ns in running[""]["nsids"].values():
        if ns == "":
            continue
        addrs = ip(ns, "addr", "show")
        running[ns] = {
            "addr_names": {a["ifname"]: a for a in addrs},
            "addr_ids": {a["ifindex"]: a for a in addrs},
            "nsids": get_nsids(ns),
        }

    return running


def preprocess(conf, args):
    out = {}
    for ns, nsconfig in conf.items():
        for addr in nsconfig["addr_names"].values():
            if addr.get("link_type") == "loopback" and not args.local:
                continue
            ethtool = {}
            try:
                cmd = ["ethtool", "-i", addr["ifname"]]
                if ns != "":
                    cmd = ["ip", "netns", "exec", ns] + cmd
                stdout = subprocess.check_output(cmd, stderr=subprocess.DEVNULL)
                for line in stdout.decode("utf-8").splitlines():
                    if ":" not in line:
                        continue
                    k, v = line.split(": ", 1)
                    ethtool[k] = v.strip()
            except subprocess.CalledProcessError:
                pass

            attributes = {}

            if "linkinfo" in addr and "info_kind" in addr["linkinfo"]:
                kind = addr["linkinfo"]["info_kind"]
            elif ethtool.get("driver", "") not in ("", "N/A"):
                kind = ethtool["driver"]
                if ethtool.get("bus-info", "") not in ("", "N/A"):
                    attributes["bus"] = ethtool["bus-info"]
            elif "link_type" in addr:
                kind = addr["link_type"]
            else:
                kind = "???"

            data = addr.get("linkinfo", {}).get("info_data", {})
            if "link" in addr:
                link_ns = ns
                link_dev = addr["link"]
            elif "link_netnsid" in addr and "link_index" in addr:
                link_ns = nsconfig["nsids"].get(addr["link_netnsid"])
                link_ids = conf.get(link_ns, {}).get("addr_ids", {})
                if addr["link_index"] in link_ids:
                    link_dev = link_ids[addr["link_index"]]["ifname"]
                else:
                    link_dev = None
            else:
                link_ns = ns
                link_dev = addr.get("linkinfo", {}).get("info_data", {}).get("link")

            if kind == "vxlan":
                attributes["id"] = data["id"]
                if "local" in data:
                    attributes["local"] = data["local"]
                if "remote" in data:
                    attributes["remote"] = data["remote"]
                elif "group" in data:
                    attributes["group"] = data["group"]
            elif kind == "bond":
                attributes["mode"] = data["mode"]
                if data["ad_lacp_active"] == "on":
                    attributes["lacp"] = data["ad_lacp_rate"]
            elif kind == "vlan":
                attributes["id"] = data["id"]

            vlans = set()
            if addr.get("linkinfo", {}).get("info_slave_kind") == "bridge":
                for p in bridge(ns, "vlan", "show", "dev", addr["ifname"]):
                    if p.get("ifname") != addr["ifname"]:
                        continue
                    for v in p.get("vlans", []):
                        if {"PVID", "Egress Untagged"} <= set(v.get("flags", [])):
                            # ignore access private vlans
                            continue
                        if "vlanEnd" in v:
                            vlans.update(range(v["vlan"], v["vlanEnd"] + 1))
                        else:
                            vlans.add(v["vlan"])

            tip = []
            if "ifalias" in addr:
                tip.append(f"alias {addr['ifalias']}")
            tip += [f"{k} {v}" for k, v in data.items()]
            l2 = []
            if "address" in addr:
                if args.l2_addresses:
                    l2.append(addr["address"])
                else:
                    tip.append(f"lladdr {addr['address']}")

            ipv4 = []
            ipv6 = []
            for a in addr.get("addr_info", []):
                if a["family"] == "inet":
                    net = f"{a['local']}/{a['prefixlen']}"
                    if args.ipv4_addresses and (a["scope"] == "global" or args.local):
                        ipv4.append(net)
                    else:
                        tip.append(f"{a['family']} {net}")
                elif a["family"] == "inet6":
                    net = f"{a['local']}/{a['prefixlen']}"
                    if args.ipv6_addresses and (a["scope"] == "global" or args.local):
                        ipv6.append(net)
                    else:
                        tip.append(f"{a['family']} {net}")

            a = {
                "id": safe(f"{ns}_{addr['ifname']}"),
                "name": addr["ifname"],
                "kind": kind,
                "attributes": attributes,
                "l2": l2,
                "vlans": vlans,
                "ipv4": ipv4,
                "ipv6": ipv6,
                "tip": tip,
            }
            if "master" in addr:
                a["master"] = safe(f"{ns}_{addr['master']}")
            if link_dev is not None:
                a["link"] = safe(f"{link_ns}_{link_dev}")
            if "ifalias" in addr:
                a["alias"] = addr["ifalias"]

            out.setdefault(ns, []).append(a)

    return out


if __name__ == "__main__":
    sys.exit(main())
