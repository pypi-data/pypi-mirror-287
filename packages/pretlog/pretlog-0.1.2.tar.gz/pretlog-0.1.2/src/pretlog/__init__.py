"""
Python module for colored output in terminal.

Can also modify line start, end and separator characters.

Example:
    import col

    col.set_cont(beg = ">>> ", sep = " -> ", end = "<<<\n")
    col.error("This is an error message.")
    col.warning("This is a warning message.")
    col.info("This is an info message.")
    col.valid("This is a valid message.")
    col.default("This is a default message.", "With multiple arguments.")
"""

from .col import (
    set_cont,
    error,
    warning,
    info,
    valid,
    default,
    new_block,
    decorate,
    err,
    warn,
    note,
    ok,
)
