# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2024 Robin Jarry


# ------------------------------------------------------------------------------
def human_readable(value: float, order: int = 1000) -> str:
    if order == 1000:
        units = ("K", "M", "G", "T")
    elif order == 1024:
        units = ("Ki", "Mi", "Gi", "Ti")
    else:
        raise ValueError("order must be 1000 or 1024")
    i = 0
    unit = ""
    while value >= order and i < len(units):
        unit = units[i]
        value /= order
        i += 1
    if unit == "":
        return str(value)
    if value < (order / 10):
        return f"{value:.1f}{unit}"
    return f"{value:.0f}{unit}"


# ------------------------------------------------------------------------------
def parse_human_readable(value: str, order: int = 1000) -> int:
    if order == 1000:
        units = ("K", "M", "G", "T")
    elif order == 1024:
        units = ("Ki", "Mi", "Gi", "Ti")
    else:
        raise ValueError("order must be 1000 or 1024")
    m = multiplier = 1
    for u in units:
        m *= order
        if value.endswith(u):
            value = value.removesuffix(u)
            multiplier = m
            break
    return float(value) * multiplier
