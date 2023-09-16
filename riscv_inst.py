"""
RISC-V Instruction Set Architecture (ISA) definitions.
"""

from bin_num import BinNum

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
RISCV_TYPE_FORMATS = {
    # RISCV_TYPE_ID: (MACHINE_CODE_FORMAT, ASSEMBLY_FORMAT)
    RISCV_TYPE_R: (
        lambda op, funct3, funct7, rd, rs1, rs2, imm: "".join(
            [
                funct7.get_bits(6, 0),
                rs2.get_bits(4, 0),
                rs1.get_bits(4, 0),
                funct3.get_bits(2, 0),
                rd.get_bits(4, 0),
                op.get_bits(6, 0),
            ]
        ),
        lambda params: {
            "rd": params[0],
            "rs1": params[1],
            "rs2": params[2],
            "imm": None,
        }
        if len(params) == 3
        else None,
    ),
    RISCV_TYPE_I: (
        lambda op, funct3, funct7, rd, rs1, rs2, imm: "".join(
            [
                imm.get_bits(11, 0),
                rs1.get_bits(4, 0),
                funct3.get_bits(2, 0),
                rd.get_bits(4, 0),
                op.get_bits(6, 0),
            ]
        ),
        lambda params: {
            "rd": params[0],
            "rs1": params[1],
            "rs2": None,
            "imm": params[2],
        }
        if len(params) == 3
        else None,
    ),
    RISCV_TYPE_S: (
        lambda op, funct3, funct7, rd, rs1, rs2, imm: "".join(
            [
                imm.get_bits(11, 5),
                rs2.get_bits(4, 0),
                rs1.get_bits(4, 0),
                funct3.get_bits(2, 0),
                imm.get_bits(4, 0),
                op.get_bits(6, 0),
            ]
        ),
        lambda params: {
            "rd": None,
            "rs1": params[1],
            "rs2": params[0],
            "imm": params[2],
        }
        if len(params) == 3
        else None,
    ),
    RISCV_TYPE_B: (
        lambda op, funct3, funct7, rd, rs1, rs2, imm: "".join(
            [
                imm.get_bits(12, 12),
                imm.get_bits(10, 5),
                rs2.get_bits(4, 0),
                rs1.get_bits(4, 0),
                funct3.get_bits(2, 0),
                imm.get_bits(4, 1),
                imm.get_bits(11, 11),
                op.get_bits(6, 0),
            ]
        ),
        lambda params: {
            "rd": None,
            "rs1": params[0],
            "rs2": params[1],
            "imm": params[2],  # Label
        }
        if len(params) == 3
        else None,
    ),
    RISCV_TYPE_U: (
        lambda op, funct3, funct7, rd, rs1, rs2, imm: "".join(
            [
                imm.get_bits(31, 12),
                rd.get_bits(4, 0),
                op.get_bits(6, 0),
            ]
        ),
        lambda params: {
            "rd": params[0],
            "rs1": None,
            "rs2": None,
            "imm": params[1],
        }
        if len(params) == 2
        else None,
    ),
    RISCV_TYPE_J: (
        lambda op, funct3, funct7, rd, rs1, rs2, imm: "".join(
            [
                imm.get_bits(20, 20),
                imm.get_bits(10, 1),
                imm.get_bits(11, 11),
                imm.get_bits(19, 12),
                rd.get_bits(4, 0),
                op.get_bits(6, 0),
            ]
        ),
        lambda params: {
            "rd": params[0],
            "rs1": None,
            "rs2": None,
            "imm": params[1],  # Label
        }
        if len(params) == 2
        else None,
    ),
}


class Inst:
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
        self._format_mc = RISCV_TYPE_FORMATS[self._type][0]
        self._format_asm = RISCV_TYPE_FORMATS[self._type][1]

        # op
        if op_code < 0 or op_code > 0x7F:  # 7 bits
            raise ValueError("Invalid op value")
        self._op = BinNum(op_code)

        # funct3
        if funct3 < 0 or funct3 > 0x7:  # 3 bits
            raise ValueError("Invalid funct3 value")
        self._funct3 = BinNum(funct3)

        # funct7
        if funct7 < 0 or funct7 > 0x7F:  # 7 bits
            raise ValueError("Invalid funct7 value")
        self._funct7 = BinNum(funct7)

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
        return self._op.get_bits(6, 0)

    @property
    def funct3(self):
        """
        Returns the funct3 value of the current instruction.
        """
        return self._funct3.get_bits(2, 0)

    @property
    def funct7(self):
        """
        Returns the funct7 value of the current instruction.
        """
        return self._funct7.get_bits(6, 0)

    def asm_params(self, params: tuple) -> dict:
        """
        Returns the assembly parameters of the current instruction.

        Args:
            params: The parameters of the instruction.

        Returns:
            The assembly parameters of the instruction.

        Raises:
            ValueError: If any of the values are invalid.
        """

        # Validate
        if not isinstance(params, tuple):
            raise ValueError("Invalid params value")

        # Format instruction
        return self._format_asm(params)

    def compile(self, rd: int, rs1: int, rs2: int, imm: int) -> BinNum:
        """
        Compiles the current instruction using the given format.

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
        if rs1 < 0 or rs1 > 0x1F:  # 5 bits
            raise ValueError("Invalid rs1 value")
        # rs2
        if rs2 < 0 or rs2 > 0x1F:  # 5 bits
            raise ValueError("Invalid rs2 value")
        # imm
        if imm < -0x80000000 or imm > 0x7FFFFFFF:  # 32 bits
            raise ValueError("Invalid imm value")

        # Format instruction
        inst_str = self._format_mc(
            op=self._op,
            funct3=self._funct3,
            funct7=self._funct7,
            rd=BinNum(rd),
            rs1=BinNum(rs1),
            rs2=BinNum(rs2),
            imm=BinNum(imm),
        )

        return BinNum(int(inst_str, 2))
