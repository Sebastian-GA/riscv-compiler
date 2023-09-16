"""
This module contains the BinNum class, which represents a 32-bit binary number.
"""


class BinNum:
    """
    Class representing a 32-bit binary number.
    """

    def __init__(self, value: int) -> None:
        """
        Initializes a binary number.
        """
        self._value = value

    @property
    def value(self) -> int:
        """
        Returns the value of the binary number.
        """
        return self._value

    @property
    def value_strb(self) -> str:
        """
        Returns the value of the binary number as a string.
        """
        return f"{(self.value & 2**32-1):032b}"

    @property
    def value_strh(self) -> str:
        """
        Returns the value of the hexadecimal number as a string.
        """
        return f"{(self.value & 2**32-1):08x}"

    def get_bits(self, top: int, bottom: int) -> int:
        """
        Returns bits top to bottom (inclusive) of the binary number.
        """
        return self.value_strb[(32 - 1) - top : 32 - bottom]

    def __str__(self) -> str:
        return self.value_strb
