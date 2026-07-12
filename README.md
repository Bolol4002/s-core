# s-core

A small digital design project written in SystemVerilog with cocotb-based verification testbenches.

## Overview

This repository currently contains a set of basic digital logic modules and their testbenches:

- ALU: a simple arithmetic and logic unit supporting add, subtract, AND, and OR operations
- NAND gate: a basic two-input NAND implementation
- Program counter (PC): a clocked register that stores the next program counter value
- Register file: a simple 32-register memory block with write-enable support

## Project Structure

- src/ - SystemVerilog source files
  - alu.sv
  - nand.sv
  - pc.sv
  - regfile.sv
- tb/ - cocotb testbenches
  - alu/
  - nand/
  - pc/
  - regfile/
- Makefile - cleanup target for generated simulation artifacts

## Verification

Each module has a cocotb testbench under its corresponding directory in tb/.

### Running tests

Navigate to a testbench directory and run:

```bash
make
```

Example:

```bash
cd tb/pc
make
```

## Current Status

The following components are implemented and verified:

- ALU module and testbench
- NAND gate module and testbench
- PC module and testbench
- Register file module and testbench

The testbenches use cocotb with Icarus Verilog simulation and validate basic functional behavior for each design.


## Plan 
| Step | Module | You'll Learn | | ---- | ------------------- | ---------------------------------------------------------- | | 1 | ALU | Combinational logic, always_comb, enums, case statements | | 2 | Register File | Arrays, synchronous writes, asynchronous reads | | 3 | Program Counter | Sequential logic, reset | | 4 | PC + 4 Adder | Simple combinational datapath | | 5 | Instruction Memory | ROM, $readmemh | | 6 | Instruction Decoder | Bit slicing | | 7 | ALU Control | Decode logic | | 8 | Control Unit | Control signal generation | | 9 | CPU Top | Module integration | | 10 | Cocotb tests | Verification | | 11 | Add I-type | Immediate generation | | 12 | Pipeline | IF/ID, ID/EX, EX/MEM, MEM/WB |