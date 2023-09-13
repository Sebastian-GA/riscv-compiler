"""
This module defines the RISC-V instruction set architecture (ISA) and provides
a dictionary of RISC-V instructions and pseudo-instructions.
"""

from riscv import (
    RISCV_TYPE_B,
    RISCV_TYPE_I,
    RISCV_TYPE_J,
    RISCV_TYPE_R,
    RISCV_TYPE_S,
    RISCV_TYPE_U,
)
from riscv import RISCVInstruction as ris

RISCV_INSTRUCTIONS = {
    # RV32I Base Instruction Set
    "lb": ris(RISCV_TYPE_I, 3, funct3=0b000),
    "lh": ris(RISCV_TYPE_I, 3, funct3=0b001),
    "lw": ris(RISCV_TYPE_I, 3, funct3=0b010),
    "lbu": ris(RISCV_TYPE_I, 3, funct3=0b100),
    "lhu": ris(RISCV_TYPE_I, 3, funct3=0b101),
    "addi": ris(RISCV_TYPE_I, 19, funct3=0b000),
    "slli": ris(RISCV_TYPE_I, 19, funct3=0b001, funct7=0b0000000),
    "slti": ris(RISCV_TYPE_I, 19, funct3=0b010),
    "sltiu": ris(RISCV_TYPE_I, 19, funct3=0b011),
    "xori": ris(RISCV_TYPE_I, 19, funct3=0b100),
    "srli": ris(RISCV_TYPE_I, 19, funct3=0b101, funct7=0b0000000),
    "srai": ris(RISCV_TYPE_I, 19, funct3=0b101, funct7=0b0100000),
    "ori": ris(RISCV_TYPE_I, 19, funct3=0b110),
    "andi": ris(RISCV_TYPE_I, 19, funct3=0b111),
    "auipc": ris(RISCV_TYPE_U, 23),
    "sb": ris(RISCV_TYPE_S, 35, funct3=0b000),
    "sh": ris(RISCV_TYPE_S, 35, funct3=0b001),
    "sw": ris(RISCV_TYPE_S, 35, funct3=0b010),
    "add": ris(RISCV_TYPE_R, 51, funct3=0b000, funct7=0b0000000),
    "sub": ris(RISCV_TYPE_R, 51, funct3=0b000, funct7=0b0100000),
    "sll": ris(RISCV_TYPE_R, 51, funct3=0b001, funct7=0b0000000),
    "slt": ris(RISCV_TYPE_R, 51, funct3=0b010, funct7=0b0000000),
    "sltu": ris(RISCV_TYPE_R, 51, funct3=0b011, funct7=0b0000000),
    "xor": ris(RISCV_TYPE_R, 51, funct3=0b100, funct7=0b0000000),
    "srl": ris(RISCV_TYPE_R, 51, funct3=0b101, funct7=0b0000000),
    "sra": ris(RISCV_TYPE_R, 51, funct3=0b101, funct7=0b0100000),
    "or": ris(RISCV_TYPE_R, 51, funct3=0b110, funct7=0b0000000),
    "and": ris(RISCV_TYPE_R, 51, funct3=0b111, funct7=0b0000000),
    "lui": ris(RISCV_TYPE_U, 55),
    "beq": ris(RISCV_TYPE_B, 99, funct3=0b000),
    "bne": ris(RISCV_TYPE_B, 99, funct3=0b001),
    "blt": ris(RISCV_TYPE_B, 99, funct3=0b100),
    "bge": ris(RISCV_TYPE_B, 99, funct3=0b101),
    "bltu": ris(RISCV_TYPE_B, 99, funct3=0b110),
    "bgeu": ris(RISCV_TYPE_B, 99, funct3=0b111),
    "jalr": ris(RISCV_TYPE_I, 103, funct3=0b000),
    "jal": ris(RISCV_TYPE_J, 111),
}

RISCV_PSEUDO_INSTRUCTIONS = {
    "nop": "addi x0, x0, 0",
    "li": "addi {0}, x0, {1}",  # TODO: There are two versions of this instruction
    "mv": "addi {0}, {1}, 0",
    "not": "xori {0}, {1}, -1",
    "neg": "sub {0}, x0, {1}",
    "seqz": "sltiu {0}, {1}, 1",
    "snez": "sltu {0}, x0, {1}",
    "sltz": "slt {0}, {1}, x0",
    "sgtz": "slt {0}, x0, {1}",
    "beqz": "beq {0}, x0, {1}",
    "bnez": "bne {0}, x0, {1}",
    "blez": "bge x0, {0}, {1}",
    "bgez": "bge {0}, x0, {1}",
    "bltz": "blt {0}, x0, {1}",
    "bgtz": "blt x0, {0}, {1}",
    "ble": "bge {1}, {0}, {2}",
    "bgt": "blt {1}, {0}, {2}",
    "bleu": "bgeu {1}, {0}, {2}",
    "bgtu": "bltu {1}, {0}, {2}",
    "j": "jal x0, {0}",
    "jal": "jal ra, {0}",
    "jr": "jalr x0, {0}, 0",
    "jalr": "jalr ra, {0}, 0",
    "ret": "jalr x0, ra, 0",
    # TODO: Finish the rest of the pseudo instructions
}
