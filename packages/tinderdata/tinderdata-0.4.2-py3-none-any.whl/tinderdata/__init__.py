"""
tinderdata Library
~~~~~~~~~~~~~~~~~~~
tinderdata is a utility library, written in Python, to handle the json given by Tinder when
requesting your usage data. It provides a high-level class with methods to print out insights,
or plot more complicated ones.

:copyright: (c) 2019-2020 by Felix Soubelet.
:license: MIT, see LICENSE for more details.
"""

from .tinder import TinderData  # noqa: TID252

__version__ = "0.4.2"

__all__ = ["TinderData"]
