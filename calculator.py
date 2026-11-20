"""
Thin wrapper around math_lib operations.

Keeping this file in the *parent* repo shows how application code
can depend on a submodule library without copying its source.
"""

from __future__ import annotations

from typing import Iterable


def safe_divide(a: float, b: float) -> float | None:
    """
    Divide a by b, returning None instead of crashing on zero.

    This function expects math_lib to be importable (via submodule path).
    """
    from math_lib import divide

    try:
        return divide(a, b)
    except ZeroDivisionError:
        return None


def summarize(numbers: Iterable[float]) -> dict[str, float]:
    """
    Return a small summary dict for a list of numbers.

    Keys:
        count  — how many numbers were given
        sum    — total of all numbers
        avg    — arithmetic mean
    """
    from math_lib import add, average

    values = list(numbers)
    total = 0.0
    for value in values:
        total = add(total, value)

    return {
        "count": float(len(values)),
        "sum": total,
        "avg": average(values) if values else 0.0,
    }
