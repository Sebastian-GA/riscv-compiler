"""
RISC-V Instruction Set Architecture (ISA) definitions.
"""

# pylint allow 1-2 letter variable names
# pylint: disable=invalid-name

# RISCV Instruction Types
RISCV_TYPE_R = 0x1
RISCV_TYPE_I = 0x2
RISCV_TYPE_S = 0x3
RISCV_TYPE_B = 0x4
RISCV_TYPE_U = 0x5
RISCV_TYPE_J = 0x6
RISCV_TYPE_MAX = 0x6
# RISCV_TYPE_R4 = 0x7  # Not supported

# RISCV Registers (x0-x31)
RISCV_REGISTERS = {
    "zero": 0,
    "ra": 1,
    "sp": 2,
    "gp": 3,
    "tp": 4,
    "t0": 5,
    "t1": 6,
    "t2": 7,
    "s0": 8,
    "fp": 8,
    "s1": 9,
    "a0": 10,
    "a1": 11,
    "a2": 12,
    "a3": 13,
    "a4": 14,
    "a5": 15,
    "a6": 16,
    "a7": 17,
    "s2": 18,
    "s3": 19,
    "s4": 20,
    "s5": 21,
    "s6": 22,
    "s7": 23,
    "s8": 24,
    "s9": 25,
    "s10": 26,
    "s11": 27,
    "t3": 28,
    "t4": 29,
    "t5": 30,
    "t6": 31,
}


class RISCVInstruction:
    """
    Class representing a RISC-V instruction.
    """

    def __init__(
        self, inst_type: int, op_code: int, funct3: int = None, funct7: int = None
    ) -> None:
        """
        Initializes a RISC-V instruction.

        Args:
            inst_type: The type of instruction.
            op_code: The opcode of the instruction.
            funct3: The funct3 value of the instruction.
            funct7: The funct7 value of the instruction.

        Raises:
            ValueError: If any of the values are invalid.
        """

        # type
        if inst_type < 1 or inst_type > RISCV_TYPE_MAX:
            raise ValueError("Invalid type value")
        self._type = inst_type

        # op
        if op_code < 0 or op_code > 0x7F:  # 7 bits
            raise ValueError("Invalid op value")
        self._op = op_code

        # funct3
        if funct3 < 0 or funct3 > 0x7:  # 3 bits
            raise ValueError("Invalid funct3 value")
        self._funct3 = funct3

        # funct7
        if funct7 < 0 or funct7 > 0x7F:  # 7 bits
            raise ValueError("Invalid funct7 value")
        self._funct7 = funct7

        # non-specific parameters of the instruction
        self._rd = 0x0
        self._rs1 = 0x0
        self._rs2 = 0x0
        self._imm = 0x0

    @property
    def type(self):
        """
        Returns the type of the current instruction.

        Types:
            RISCV_TYPE_R = 0x1
            RISCV_TYPE_I = 0x2
            RISCV_TYPE_S = 0x3
            RISCV_TYPE_B = 0x4
            RISCV_TYPE_U = 0x5
            RISCV_TYPE_J = 0x6
            RISCV_TYPE_R4 = 0x7
        """
        return self._type

    @property
    def op(self):
        """
        Returns the opcode of the current instruction.
        """
        return self._op

    @property
    def funct3(self):
        """
        Returns the funct3 value of the current instruction.
        """
        return self._funct3

    @property
    def funct7(self):
        """
        Returns the funct7 value of the current instruction.
        """
        return self._funct7
