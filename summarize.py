#!/usr/bin/env python3
"""Materialize the requested summary through the tracked review engine."""
from report import render


def summarize():
    """Return the complete repository summary."""
    return render()


if __name__ == "__main__":
    print(summarize(), end="")
