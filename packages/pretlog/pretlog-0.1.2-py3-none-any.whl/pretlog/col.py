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

import os
from colorama import Fore

_cont: list[str] = ["", " ", "\n"]


def set_cont(beg: str = "", sep: str = " ", end: str = "\n") -> None:
    """
    Function to modify line start, end and separator characters.

    Parameters:
        * beg: Line start character. Default is "".
        * sep: Separator character. Default is " ".
        * end: Line end character. Default is "\n".
    """
    _cont[0] = beg
    _cont[1] = sep
    _cont[2] = end


def error(*s: str, beg: str = None, end: str = None, sep: str = None) -> None:
    """
    Function to print an error message (in red). Same interface as `default`.
    """
    print(
        Fore.RED
        + (beg if beg is not None else _cont[0])
        + (sep if sep is not None else _cont[1]).join([str(si) for si in s])
        + (end if end is not None else _cont[2])
        + Fore.RESET,
        end="",
    )


err = error


def warning(*s: str, beg: str = None, end: str = None, sep: str = None) -> None:
    """
    Function to print an warning message (in yellow). Same interface as `default`.
    """
    print(
        Fore.YELLOW
        + (beg if beg is not None else _cont[0])
        + (sep if sep is not None else _cont[1]).join([str(si) for si in s])
        + (end if end is not None else _cont[2])
        + Fore.RESET,
        end="",
    )


warn = warning


def info(*s: str, beg: str = None, end: str = None, sep: str = None) -> None:
    """
    Function to print an info message (in blue). Same interface as `default`.
    """
    print(
        Fore.BLUE
        + (beg if beg is not None else _cont[0])
        + (sep if sep is not None else _cont[1]).join([str(si) for si in s])
        + (end if end is not None else _cont[2])
        + Fore.RESET,
        end="",
    )


note = info


def valid(*s: str, beg: str = None, end: str = None, sep: str = None) -> None:
    """
    Function to print a valid message (in green). Same interface as `default`.
    """
    print(
        Fore.GREEN
        + (beg if beg is not None else _cont[0])
        + (sep if sep is not None else _cont[1]).join([str(si) for si in s])
        + (end if end is not None else _cont[2])
        + Fore.RESET,
        end="",
    )


ok = valid


def default(*s: str, beg: str = None, end: str = None, sep: str = None) -> None:
    """
    Function to print a normal message (in white).

    Parameters:
        * *s: Strings to print.
        * beg: Line start character. Default is "".
        * sep: Separator character. Default is " ".
        * end: Line end character. Default is "\n".

    """
    print(
        Fore.RESET
        + (beg if beg is not None else _cont[0])
        + (sep if sep is not None else _cont[1]).join([str(si) for si in s])
        + (end if end is not None else _cont[2])
        + Fore.RESET,
        end="",
    )


def new_block(sep: str = "█"):
    """
    Function to isolate blocks of output.

    Useful for periodic programs.

    Parameters:
        * sep: Separator character. Default is "█".
            Will be replicated to fill the terminal width.
    """
    print(sep * os.get_terminal_size()[0])


def decorate(s: str, col=Fore.RED, _next=Fore.RESET) -> str:
    """
    Function to colorize any string with a given color.

    Parameters:
        * s: String to colorize.
        * col: Color to use. Default is red.
        * next: Next color to use. Default is reset.
    Return:
        * Colored string.
    """
    return col + s + _next


deco = decorate
