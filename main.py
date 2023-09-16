"""
RISC-V Compiler
"""

import riscv

print(riscv.insts["add"].compile(riscv.regs["a0"], 0, 0, 0))
