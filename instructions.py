"""
This module defines the RISC-V instruction set architecture (ISA) and provides
a dictionary of RISC-V instructions and pseudo-instructions.
"""

# pylint allow 1-2 letter variable names
# pylint: disable=invalid-name

import riscv_inst
from riscv_inst import Inst

insts = {
    # RV32I Base Instruction Set
    "lb": Inst(riscv_inst.RISCV_TYPE_I, 3, funct3=0b000),
    "lh": Inst(riscv_inst.RISCV_TYPE_I, 3, funct3=0b001),
    "lw": Inst(riscv_inst.RISCV_TYPE_I, 3, funct3=0b010),
    "lbu": Inst(riscv_inst.RISCV_TYPE_I, 3, funct3=0b100),
    "lhu": Inst(riscv_inst.RISCV_TYPE_I, 3, funct3=0b101),
    "addi": Inst(riscv_inst.RISCV_TYPE_I, 19, funct3=0b000),
    "slli": Inst(riscv_inst.RISCV_TYPE_I, 19, funct3=0b001, funct7=0b0000000),
    "slti": Inst(riscv_inst.RISCV_TYPE_I, 19, funct3=0b010),
    "sltiu": Inst(riscv_inst.RISCV_TYPE_I, 19, funct3=0b011),
    "xori": Inst(riscv_inst.RISCV_TYPE_I, 19, funct3=0b100),
    "srli": Inst(riscv_inst.RISCV_TYPE_I, 19, funct3=0b101, funct7=0b0000000),
    "srai": Inst(riscv_inst.RISCV_TYPE_I, 19, funct3=0b101, funct7=0b0100000),
    "ori": Inst(riscv_inst.RISCV_TYPE_I, 19, funct3=0b110),
    "andi": Inst(riscv_inst.RISCV_TYPE_I, 19, funct3=0b111),
    "auipc": Inst(riscv_inst.RISCV_TYPE_U, 23),
    "sb": Inst(riscv_inst.RISCV_TYPE_S, 35, funct3=0b000),
    "sh": Inst(riscv_inst.RISCV_TYPE_S, 35, funct3=0b001),
    "sw": Inst(riscv_inst.RISCV_TYPE_S, 35, funct3=0b010),
    "add": Inst(riscv_inst.RISCV_TYPE_R, 51, funct3=0b000, funct7=0b0000000),
    "sub": Inst(riscv_inst.RISCV_TYPE_R, 51, funct3=0b000, funct7=0b0100000),
    "sll": Inst(riscv_inst.RISCV_TYPE_R, 51, funct3=0b001, funct7=0b0000000),
    "slt": Inst(riscv_inst.RISCV_TYPE_R, 51, funct3=0b010, funct7=0b0000000),
    "sltu": Inst(riscv_inst.RISCV_TYPE_R, 51, funct3=0b011, funct7=0b0000000),
    "xor": Inst(riscv_inst.RISCV_TYPE_R, 51, funct3=0b100, funct7=0b0000000),
    "srl": Inst(riscv_inst.RISCV_TYPE_R, 51, funct3=0b101, funct7=0b0000000),
    "sra": Inst(riscv_inst.RISCV_TYPE_R, 51, funct3=0b101, funct7=0b0100000),
    "or": Inst(riscv_inst.RISCV_TYPE_R, 51, funct3=0b110, funct7=0b0000000),
    "and": Inst(riscv_inst.RISCV_TYPE_R, 51, funct3=0b111, funct7=0b0000000),
    "lui": Inst(riscv_inst.RISCV_TYPE_U, 55),
    "beq": Inst(riscv_inst.RISCV_TYPE_B, 99, funct3=0b000),
    "bne": Inst(riscv_inst.RISCV_TYPE_B, 99, funct3=0b001),
    "blt": Inst(riscv_inst.RISCV_TYPE_B, 99, funct3=0b100),
    "bge": Inst(riscv_inst.RISCV_TYPE_B, 99, funct3=0b101),
    "bltu": Inst(riscv_inst.RISCV_TYPE_B, 99, funct3=0b110),
    "bgeu": Inst(riscv_inst.RISCV_TYPE_B, 99, funct3=0b111),
    "jalr": Inst(riscv_inst.RISCV_TYPE_I, 103, funct3=0b000),
    "jal": Inst(riscv_inst.RISCV_TYPE_J, 111),
}

pinsts = {
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
