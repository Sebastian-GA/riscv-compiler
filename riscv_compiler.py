"""
RISC-V Compiler
"""

# pylint allow 1-2 letter variable names
# pylint: disable=invalid-name

import instructions as riscv_insts
import registers as riscv_regs
from bin_num import BinNum


class Compiler:
    """
    RISC-V Compiler
    """

    @staticmethod
    def get_line_params(line: str) -> tuple:
        """
        Get instruction and parameters from line
        """
        line = line.strip()  # Remove leading and trailing whitespace
        line = line.split("#")[0]  # Remove comments
        inst, *params = line.split(" ")

        # Split params
        params = "".join(params).replace(" ", "").split(",")
        ## If instruction is load or store, split offset from last param
        if "(" in params[-1]:
            offset = params[-1].split("(")
            params[-1] = offset[1].replace(")", "")
            params.append(offset[0])  # Add offset to params

        return (inst, tuple(params))

    @staticmethod
    def convert_param(param: str) -> int or str:
        """
        Convert parameter to number
        """
        if param is None:
            return 0  # Default value for unused parameters

        # Check if parameter is register
        if param in riscv_regs.regs:
            return riscv_regs.regs[param]
        elif param[0] == "x" and param[1:].isdigit():
            if int(param[1:]) < 0 or int(param[1:]) > 31:
                raise ValueError(f"Invalid parameter: {param}")
            return int(param[1:])

        # Check if parameter is immediate
        if param.isdigit():
            return int(param)

        # Then must be label!
        if param[-1] != ":":
            raise ValueError(f"Invalid parameter: {param}")
        return param[:-1]
        # TODO: Add support for labels

    @staticmethod
    def compile(file):
        """
        Compile assembly file to machine code
        """
        # Read file
        with open(file, "r", encoding="utf-8") as asm:
            lines = asm.readlines().split("\n")

        machine_code = []
        for line in lines:
            if line == "":
                continue
            # TODO: First build labels dict
            machine_code.append(Compiler.compile_line(line))

    @staticmethod
    def compile_line(line: str, pc: int = 0, labels: dict = None) -> BinNum:
        """
        Compile assembly line to machine code
        """
        if labels is None:
            labels = {}

        # Get instruction and parameters
        inst, params_tpl = Compiler.get_line_params(line)

        # Check if instruction is pseudo-instruction
        if inst in riscv_insts.pinsts:
            # TODO: Add support for pseudo-instructions
            pass

        # Check if instruction is valid
        elif inst not in riscv_insts.insts:
            raise ValueError(f"Invalid instruction: {inst} in line {pc // 4 + 1}")

        # Check if parameters are valid
        params_dict = riscv_insts.insts[inst].asm_params(params_tpl)
        if params_dict is None:
            raise ValueError(f"Invalid parameters: {params_tpl} in line {pc // 4 + 1}")

        # Convert parameters to numbers
        params_dict = {k: Compiler.convert_param(v) for k, v in params_dict.items()}

        # Convert labels to offsets
        if params_dict["imm"] in labels:
            # TODO: Convert label to offset
            # params_dict["imm"] = labels[params_dict["imm"]]
            pass

        # Compile instruction
        inst_bin = riscv_insts.insts[inst].compile(**params_dict)

        return inst_bin
