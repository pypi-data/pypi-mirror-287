# -*- coding: utf-8 -*-

"""
server monitoring measurement command line user interface.

See :class:`Command` for details.
"""

import fire

from .._version import __version__


class Command:
    """
    Acore Soap Agent command line interface. All these commands can only be
    used on EC2.
    """

    def hello(self):
        """
        Print welcome message.
        """
        print(f"Hello acore_server_monitoring_measurement {__version__} user!")

    def version(self):
        """
        Print version number.
        """
        print(__version__)


def run():
    fire.Fire(Command)
