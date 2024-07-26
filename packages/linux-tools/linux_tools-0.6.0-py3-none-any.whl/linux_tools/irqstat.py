#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2023-2024 Robin Jarry

"""
Display linux interrupts information.
"""

import argparse
import os
import re
import sys

from . import bits, table, util


# ------------------------------------------------------------------------------
def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-r",
        "--root",
        default="/",
        help="""
        Root dir used to determine path to /proc (default /).
        """,
    )
    parser.add_argument(
        "-c",
        "--cpu",
        type=bits.mask_or_list,
        metavar="CPU_RANGE_OR_MASK",
        action="append",
        default=[],
        help="""
        CPUs specified as an hexadecimal mask values (e.g. 0xeec2) or as a
        comma-separated list of IDs. Consecutive IDs can be compressed as ranges (e.g.
        5,6,7,8,9,10 --> 5-10). Can be used multiple times.
        """,
    )
    parser.add_argument(
        "-i",
        "--irq",
        action="append",
        default=[],
        help="""
        Only show this IRQ. Can be used multiple times. Special values are HARD (for
        numbered hardware IRQs), SOFT (for unnumbered software interrupts and
        exceptions) and ALL (for all IRQs and exceptions). By default, only numbered
        hardware IRQs are displayed.
        """,
    )
    parser.add_argument(
        "-n",
        "--num-per-cpu",
        action="store_true",
        help="""
        Display the number of bound IRQs per CPU.
        """,
    )
    parser.add_argument(
        "-s",
        "--stats",
        action="store_true",
        help="""
        Display interrupt counts.
        """,
    )
    parser.add_argument(
        "-z",
        "--display-zeroes",
        action="store_true",
        help="""
        Also show -s/--stats with 0 values.
        """,
    )
    parser.add_argument(
        "-t",
        "--threshold",
        type=util.parse_human_readable,
        default=0,
        help="""
        Hide -s/--stats below that value. Accepts human readable numbers (e.g. 1K).
        """,
    )
    parser.add_argument(
        "-e",
        "--exact",
        action="store_true",
        help="""
        Display exact stats values.
        """,
    )
    args = parser.parse_args()
    cpu_ids = set()
    for m in args.cpu:
        cpu_ids.update(m)
    irq_ids = set(args.irq)
    hardirqs = "HARD" in irq_ids or "ALL" in irq_ids or not irq_ids
    softirqs = "SOFT" in irq_ids or "ALL" in irq_ids
    irq_ids.discard("HARD")
    irq_ids.discard("SOFT")
    irq_ids.discard("ALL")

    if args.stats and args.num_per_cpu:
        parser.error("-s is not supported with -n")

    try:
        os.chdir(args.root)
        irqs = parse_proc_interrupts()
        cpus = {}
        for irq, i in irqs.items():
            for c in range(len(i["counters"])):
                cpus.setdefault(c, {"affinity": 0, "effective": 0})
            if args.stats or (irq_ids and irq not in irq_ids):
                continue
            try:
                with open(
                    f"proc/irq/{irq}/smp_affinity_list", "r", encoding="ascii"
                ) as f:
                    affinity = bits.mask_or_list(f.read().strip())
                i["affinity"] = affinity
                for c in affinity:
                    cpus[c]["affinity"] += 1
                with open(
                    f"proc/irq/{irq}/effective_affinity_list", "r", encoding="ascii"
                ) as f:
                    effective = bits.mask_or_list(f.read().strip())
                i["effective"] = effective
                for c in effective:
                    cpus[c]["effective"] += 1
            except FileNotFoundError:
                pass  # not all irqs are listed here

        if cpu_ids - cpus.keys():
            raise ValueError(f"no such CPUs: {bits.bit_list(cpu_ids - cpus.keys())}")
        if irq_ids - irqs.keys():
            raise ValueError(f"no such IRQs: {irq_ids - irqs.keys()}")

    except Exception as e:
        sys.stderr.write(f"error: {e}\n")
        sys.stderr.flush()
        return 1

    if args.exact:
        num_format = str
    else:
        num_format = util.human_readable

    for i in irqs.values():
        if not i.get("affinity"):
            i["affinity"] = set(cpus.keys())
        if not i.get("effective"):
            i["effective"] = set(cpus.keys())

    if irq_ids:
        irq_ids = list(irq_ids)
        per_cpu = True
    else:
        irq_ids = []
        for irq in irqs:
            if hardirqs and irq.isdigit() or softirqs and not irq.isdigit():
                irq_ids.append(irq)
        per_cpu = False
    if cpu_ids:
        per_irq = True
        cpu_ids = sorted(cpu_ids)
    else:
        per_irq = False
        cpu_ids = sorted(cpus.keys())
    irq_ids.sort(key=lambda i: f"{int(i):04d}" if i.isdigit() else i)

    if args.stats:
        if per_cpu:
            t = stats_table_per_cpu(
                irqs,
                cpus,
                cpu_ids,
                irq_ids,
                threshold=args.threshold,
                display_zeroes=args.display_zeroes,
                num_format=num_format,
            )
        elif per_irq:
            t = stats_table_per_irq(
                irqs,
                cpus,
                cpu_ids,
                irq_ids,
                threshold=args.threshold,
                display_zeroes=args.display_zeroes,
                num_format=num_format,
            )
        else:
            t = table.Table()
            t.add_column("IRQ")
            t.add_column("TOTAL", table.ALIGN_RIGHT, num_format)
            t.add_column("DESCRIPTION")
            for irq in irq_ids:
                i = irqs[irq]
                total = sum(i["counters"][c] for c in cpu_ids)
                if total == 0 and not args.display_zeroes:
                    continue
                if total < args.threshold:
                    continue
                t.add_row([irq, total, i["desc"]])

    elif args.num_per_cpu:
        t = table.Table()
        t.add_column("CPU")
        t.add_column("AFFINITY-IRQs", table.ALIGN_RIGHT)
        t.add_column("EFFECTIVE-IRQs", table.ALIGN_RIGHT)
        for cpu in cpu_ids:
            c = cpus[cpu]
            t.add_row([cpu, c["affinity"], c["effective"]])

    else:
        t = table.Table()
        t.add_column("IRQ")
        t.add_column("AFFINITY", table.ALIGN_RIGHT, bits.bit_list)
        t.add_column("EFFECTIVE-CPU", table.ALIGN_RIGHT, bits.bit_list)
        t.add_column("DESCRIPTION")
        for irq in irq_ids:
            i = irqs[irq]
            if cpu_ids and not i["effective"].intersection(cpu_ids):
                continue
            t.add_row([irq, i["affinity"], i["effective"], i["desc"]])

    t.print(sys.stdout)

    return 0


# ------------------------------------------------------------------------------
def stats_table_per_cpu(
    irqs: dict,
    cpus: dict,
    cpu_ids: list[int],
    irq_ids: list[str],
    threshold: float = 0.0,
    display_zeroes: bool = False,
    num_format: callable = str,
) -> table.Table:
    t = table.Table()

    lines = []
    for cpu in sorted(cpus.keys()):
        if cpu_ids and cpu not in cpu_ids:
            continue
        nums = [irqs[i]["counters"][cpu] for i in irq_ids]
        if not any(nums) and not display_zeroes:
            continue
        if all(n < threshold for n in nums):
            continue
        lines.append([cpu] + nums)

    drop_columns = []
    t.add_column("CPU")
    for i, irq in enumerate(irq_ids, 1):
        if all(
            line[i] < threshold or (line[i] == 0 and not display_zeroes)
            for line in lines
        ):
            drop_columns.append(i)
            continue
        t.add_column(
            f"IRQ-{irq}" if irq.isdigit() else irq,
            table.ALIGN_RIGHT,
            num_format,
        )
    for line in lines:
        for d in reversed(drop_columns):
            del line[d]
    for line in lines:
        t.add_row(line)

    return t


# ------------------------------------------------------------------------------
def stats_table_per_irq(
    irqs: dict,
    cpus: dict,
    cpu_ids: list[int],
    irq_ids: list[str],
    threshold: float = 0.0,
    display_zeroes: bool = False,
    num_format: callable = str,
) -> table.Table:
    t = table.Table()

    lines = []
    for irq in irq_ids:
        i = irqs[irq]
        nums = [i["counters"][c] for c in cpu_ids]
        if not any(nums) and not display_zeroes:
            continue
        if all(n < threshold for n in nums):
            continue
        lines.append([irq] + nums + [i["desc"]])

    drop_columns = []
    t.add_column("IRQ")
    for i, c in enumerate(cpu_ids, 1):
        if all(
            line[i] < threshold or (line[i] == 0 and not display_zeroes)
            for line in lines
        ):
            drop_columns.append(i)
            continue
        t.add_column(f"CPU-{c}", table.ALIGN_RIGHT, num_format)
    t.add_column("DESCRIPTION")
    for line in lines:
        for d in reversed(drop_columns):
            del line[d]
    for line in lines:
        t.add_row(line)

    return t


# ------------------------------------------------------------------------------
CPU_RE = re.compile(r"\bCPU(\d+)\b")
INTERRUPT_RE = re.compile(r"^\s*(\w+):\s+([\s\d]+)\s+([A-Za-z].+)$")
SOFTIRQS_RE = re.compile(r"^\s*(\w+):\s+([\s\d]+)\s*$")
SOFTIRQS_DESC = {
    "HI": "high priority tasklet softirq",
    "TIMER": "timer softirq",
    "NET_TX": "network transmit softirq",
    "NET_RX": "network receive softirq",
    "BLOCK": "block device softirq",
    "IRQ_POLL": "IO poll softirq",
    "TASKLET": "normal priority tasklet softirq",
    "SCHED": "schedule softirq",
    "HRTIMER": "high resolution timer softirq",
    "RCU": "RCU softirq",
}


def parse_proc_interrupts() -> (dict, dict):
    with open("proc/interrupts", "r", encoding="ascii") as f:
        interrupts = f.read().strip().splitlines()

    with open("proc/softirqs", "r", encoding="ascii") as f:
        softirqs = f.read().strip().splitlines()

    interrupts_cpu_ids = [int(c) for c in CPU_RE.findall(interrupts.pop(0))]
    softirqs_cpu_ids = [int(c) for c in CPU_RE.findall(softirqs.pop(0))]
    counters_len = max(*interrupts_cpu_ids, *softirqs_cpu_ids) + 1

    irqs = {}
    for line in interrupts:
        m = INTERRUPT_RE.match(line)
        if m is None:
            continue
        counters = [0] * counters_len
        for i, c in enumerate(m.group(2).split()):
            counters[interrupts_cpu_ids[i]] = int(c)
        irqs[m.group(1)] = {
            "desc": re.sub(r"\s+", " ", m.group(3).strip()),
            "counters": counters,
        }

    for line in softirqs:
        m = SOFTIRQS_RE.match(line)
        if m is None:
            continue
        irq = m.group(1)
        counters = [0] * counters_len
        for i, c in enumerate(m.group(2).split()):
            counters[softirqs_cpu_ids[i]] = int(c)
        irqs[irq] = {
            "desc": SOFTIRQS_DESC.get(irq, "-"),
            "counters": counters,
        }

    return irqs


# ------------------------------------------------------------------------------
if __name__ == "__main__":
    sys.exit(main())
