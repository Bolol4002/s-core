# s-core

A small digital design project written in SystemVerilog with cocotb-based verification testbenches.

## Overview

This repository contains SystemVerilog modules for a RISC-V CPU with cocotb-based verification testbenches. Currently implements the foundational datapath components of a single-cycle processor.

## Project Structure

- src/ - SystemVerilog source files
  - alu.sv - Arithmetic and logic unit (add, subtract, AND, OR operations)
  - nand.sv - Basic two-input NAND gate
  - pc.sv - Program counter with clocked register
  - regfile.sv - 32-register file with synchronous write and asynchronous read
  - pc_plus4.sv - PC + 4 adder for sequential instruction fetch
  - imem.sv - Instruction memory (ROM) loaded via $readmemh
  - idecoder.sv - Instruction decoder for extracting instruction fields
- tb/ - cocotb testbenches (one per module)
- Makefile - cleanup target for generated simulation artifacts

## Verification

Each module has a corresponding cocotb testbench under `tb/`.

### Running tests

Navigate to a testbench directory and run:

```bash
make
```

Example:

```bash
cd tb/alu
make
```

## Current Status

**Completed Modules (Steps 1-6):**

| Step | Module | Status |
|------|--------|--------|
| 1 | ALU | ✓ Implemented & Tested |
| 2 | Register File | ✓ Implemented & Tested |
| 3 | Program Counter | ✓ Implemented & Tested |
| 4 | PC + 4 Adder | ✓ Implemented & Tested |
| 5 | Instruction Memory | ✓ Implemented & Tested |
| 6 | Instruction Decoder | ✓ Implemented & Tested |

All foundational datapath components are implemented with working cocotb testbenches using Icarus Verilog.


# RISC-V CPU Development Plan

| Step | Module | Status | You'll Learn |
|------|--------|--------|--------------------------------------------------------------|
| 1 | ALU | ✓ | Combinational logic, `always_comb`, enums, `case` statements |
| 2 | Register File | ✓ | Arrays, synchronous writes, asynchronous reads |
| 3 | Program Counter | ✓ | Sequential logic, clocking, reset |
| 4 | PC + 4 Adder | ✓ | Simple combinational datapath |
| 5 | Instruction Memory | ✓ | ROM design, `$readmemh` |
| 6 | Instruction Decoder | ✓ | Bit slicing, instruction field extraction |
| 7 | ALU Control | - | Decode logic, ALU operation selection |
| 8 | Control Unit | - | Control signal generation |
| 9 | CPU Top | - | Module integration |
| 10 | Cocotb Tests | - | Verification using Cocotb |
| 11 | I-Type Instructions | - | Immediate generation and execution |
| 12 | Pipeline | - | IF/ID, ID/EX, EX/MEM, MEM/WB pipeline stages |