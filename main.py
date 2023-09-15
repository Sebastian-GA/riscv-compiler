import riscv as ris
import riscv_instructions as riscv

print(
    f'{riscv.RISCV_INSTRUCTIONS["add"].compile(ris.RISCV_REGISTERS["a0"], ris.RISCV_REGISTERS["zero"], ris.RISCV_REGISTERS["zero"], 8):x}'
)
