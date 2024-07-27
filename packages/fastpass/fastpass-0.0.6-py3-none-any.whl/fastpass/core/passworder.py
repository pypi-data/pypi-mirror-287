from __future__ import annotations

import random
import string
from typing import Iterator


class Passworder:
    """Passworder."""

    DEFAULT_SEPARATOR = "\n"

    def __init__(
        self,
        separator: str = DEFAULT_SEPARATOR,
        with_upper: bool = False,
        with_digits: bool = False,
        with_specials: bool = False,
    ) -> None:
        self._alphabet: tuple[str, ...] = self._get_alphabet(
            with_digits=with_digits,
            with_specials=with_specials,
            with_upper=with_upper,
        )

        self._random = random.SystemRandom()

        self._separator = separator

        self._with_upper = with_upper
        self._with_digits = with_digits
        self._with_specials = with_specials

    @staticmethod
    def _get_alphabet(
        with_upper: bool = False,
        with_digits: bool = False,
        with_specials: bool = False,
    ) -> tuple[str, ...]:
        alphabet = list(string.ascii_lowercase)

        if with_upper:
            alphabet.extend(list(string.ascii_uppercase))

        if with_digits:
            alphabet.extend(list(string.digits))

        if with_specials:
            alphabet.extend(list(string.punctuation))

        return tuple(alphabet)

    def _get_sequences(self, count: int, length: int) -> Iterator[str]:
        """Generator sequences.

        Args:
            count (int): sequences count
            length (int): symbols length per sequence

        Yields:
            str: sequence
        """
        for _ in range(count):
            result = None

            while not result:
                result = "".join(self._random.choice(self._alphabet) for _ in range(length))

            yield result

    def get(self, count: int, length: int) -> str:
        """Get separated sequences.

        Args:
            count (int): sequences count
            length (int): sequence length
            separator (str, optional): Defaults to '\n'.

        Returns:
            str: Sequences
        """
        pass_sequences: list[str] = []

        for seq in self._get_sequences(count, length):
            pass_sequences.append(seq)

        return f"{self._separator}".join(pass_sequences)
