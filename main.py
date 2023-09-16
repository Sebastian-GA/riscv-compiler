"""
RISC-V Compiler
"""

import riscv

print(riscv.insts["add"].compile(riscv.regs["a0"], 0, 0, 0).value_strh)
print(riscv.compiler.compile_line("add a0, zero, zero").value_strh)
