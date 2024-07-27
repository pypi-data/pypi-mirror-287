import argparse

from fastpass.__about__ import __project__, __version__
from fastpass.core.passworder import Passworder


class App:
    """App entrypoint."""

    def __init__(self) -> None:
        self._parser = argparse.ArgumentParser(prog=__project__)

    def start(self) -> None:
        """Start parse args and set to pass."""
        self._set_commands()

        command = self._parser.parse_args()

        if command.version:
            self.version()

        else:
            self._root(
                count=command.count,
                length=command.length,
                separator=command.separator,
            )

    def _set_commands(self) -> None:
        """Set command args."""

        self._parser.add_argument("--version", "-V", action="store_true", help="Print fastpass version.")

        self._parser.add_argument("--count", "-c", type=int, default=1, help="Number of passwords for generate.")
        self._parser.add_argument(
            "--length",
            "-l",
            type=int,
            default=5,
            help="Length of generated passwords.",
        )

        self._parser.add_argument(
            "--separator",
            "-S",
            type=str,
            default="\n",
            help="Separator between passwords.",
        )

    def version(self) -> None:
        """Show version."""
        print(__version__)

    def _root(  # noqa: CFQ002
        self,
        count: int = 1,
        length: int = 5,
        separator: str = "-",
        with_digits: bool = True,
        with_upper: bool = True,
        with_specials: bool = False,
    ) -> None:
        """Generate passwords."""

        generator = Passworder(
            separator=separator,
            with_upper=with_upper,
            with_digits=with_digits,
            with_specials=with_specials,
        )

        print(generator.get(count=count, length=length))
