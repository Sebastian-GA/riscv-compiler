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

# RISCV Instruction Formats
# 0: op, 1: funct3, 2: funct7, 3: rd, 4: rs1, 5: rs2, 6: imm
RISCV_TYPE_FORMATS = {
    RISCV_TYPE_R: "{funct7:7}{rs2:5}{rs1:5}{funct3:3}{rd:5}{op:7}",
    RISCV_TYPE_I: "{imm.get11_0:12}{rs1:5}{funct3:3}{rd:5}{op:7}",
    RISCV_TYPE_S: "{imm.get11_5:7}{rs2:5}{rs1:5}{funct3:3}{imm.get4_0:5}{op:7}",
    RISCV_TYPE_B: "{imm.get12:1}{imm.get10_5:6}{rs2:5}{rs1:5}{funct3:3}{imm.get4_1:4}{imm.get11:1}{op:7}",
    RISCV_TYPE_U: "{imm.get31_12:20}{rd:5}{op:7}",
    RISCV_TYPE_J: "{imm.get20:1}{imm.get10_1:10}{imm.get11:1}{imm.get19_12:8}{rd:5}{op:7}",
}

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
        self, inst_type: int, op_code: int, funct3: int = 0, funct7: int = 0
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

    def compile(self, rd: int, rs1: int, rs2: int, imm: int) -> int:
        """
        Compiles the current instruction using the given format string.

        Args:
            rd: The destination register.
            rs1: The first source register.
            rs2: The second source register.
            imm: The immediate value.

        Returns:
            The compiled instruction.

        Raises:
            ValueError: If any of the values are invalid.
        """

        # Validate

        # rd
        if rd < 0 or rd > 0x1F:  # 5 bits
            raise ValueError("Invalid rd value")
        # rs1
        if rs1 < 0 or rs1 > 0x1F:
            raise ValueError("Invalid rs1 value")
        # rs2
        if rs2 < 0 or rs2 > 0x1F:
            raise ValueError("Invalid rs2 value")
        # imm
        # if self.type == RISCV_TYPE_I and (imm < -0x800 or imm > 0x7FF):
        #     raise ValueError("Invalid imm value")
        # if self.type == RISCV_TYPE_S and (imm < -0x800 or imm > 0x7FF):
        #     raise ValueError("Invalid imm value")
        # if self.type == RISCV_TYPE_U and (imm < -0x800 or imm > 0x7FF):
        #     raise ValueError("Invalid imm value")

        # Format instruction
        inst_str = RISCV_TYPE_FORMATS[self.type].format(
            op=f"{self.op:07b}",
            funct3=f"{self.funct3:03b}",
            funct7=f"{self.funct7:07b}",
            rd=f"{rd:05b}",
            rs1=f"{rs1:05b}",
            rs2=f"{rs2:05b}",
            imm=Immediate(f"{imm:032b}"),
        )

        return int(inst_str, 2)


class Immediate:
    """
    Class representing a RISC-V imm.
    """

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        """
        Returns all 32 bits of the imm.
        """
        return self._value

    @property
    def get11_0(self):
        """
        Returns bits 11 to 0 (inclusive) of the RISC-V imm.
        """
        return self._value[(32 - 1) - 11 : 32 - 0]

    @property
    def get11_5(self):
        """
        Returns bits 11 to 5 (inclusive) of the RISC-V imm.
        """
        return self._value[(32 - 1) - 11 : 32 - 5]

    @property
    def get4_0(self):
        """
        Returns bits 4 to 0 (inclusive) of the RISC-V imm.
        """
        return self._value[(32 - 1) - 4 : 32 - 0]

    @property
    def get12(self):
        """
        Returns bit 12 of the RISC-V imm.
        """
        return self._value[(32 - 1) - 12 : 32 - 12]

    @property
    def get10_5(self):
        """
        Returns bits 10 to 5 (inclusive) of the RISC-V imm.
        """
        return self._value[(32 - 1) - 10 : 32 - 5]

    @property
    def get4_1(self):
        """
        Returns bits 4 to 1 (inclusive) of the RISC-V imm.
        """
        return self._value[(32 - 1) - 4 : 32 - 1]

    @property
    def get11(self):
        """
        Returns bit 11 of the RISC-V imm.
        """
        return self._value[(32 - 1) - 11 : 32 - 11]

    @property
    def get31_12(self):
        """
        Returns bits 31 to 12 (inclusive) of the RISC-V imm.
        """
        return self._value[(32 - 1) - 31 : 32 - 12]

    @property
    def get20(self):
        """
        Returns bit 20 of the RISC-V imm.
        """
        return self._value[(32 - 1) - 20 : 32 - 20]

    @property
    def get10_1(self):
        """
        Returns bits 10 to 1 (inclusive) of the RISC-V imm.
        """
        return self._value[(32 - 1) - 10 : 32 - 1]

    @property
    def get19_12(self):
        """
        Returns bits 19 to 12 (inclusive) of the RISC-V imm.
        """
        return self._value[(32 - 1) - 19 : 32 - 12]
