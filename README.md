# s-core

A small digital design project written in SystemVerilog with cocotb-based verification testbenches.

## Overview

This repository contains a growing set of SystemVerilog modules for a simple RISC-V-inspired single-cycle CPU, together with cocotb-based verification testbenches. The project currently includes the core datapath pieces plus a top-level CPU module that connects them together.

## Project Structure

- src/ - SystemVerilog source files
  - alu.sv - Arithmetic and logic unit supporting add, subtract, AND, and OR
  - alu_control.sv - Decodes R-type funct fields into ALU operations
  - control_unit.sv - Generates basic control signals for the current datapath
  - cpu.sv - Top-level CPU module that instantiates and connects all datapath modules
  - cpu_pkg.sv - Shared package containing opcode and ALU operation definitions
  - idecoder.sv - Instruction decoder for extracting opcode and register fields
  - imem.sv - Instruction ROM loaded via $readmemh
  - nand.sv - Basic two-input NAND gate
  - pc.sv - Program counter with synchronous update and reset
  - pc_plus4.sv - PC + 4 adder for sequential instruction fetch
  - regfile.sv - 32-entry register file with synchronous write and asynchronous read
- tb/ - cocotb testbenches, one per major module or integration point
  - alu/, alu_control/, control_unit/, cpu/, imem/, nand/, pc/, pc_plus4/, regfile/
- Makefile - Cleanup target for generated simulation artifacts

## Verification

Each module has a corresponding cocotb testbench under tb/.

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

The project currently includes the following implemented and verified components:

| Step | Module | Status |
|------|--------|--------|
| 1 | ALU | ✓ Implemented & Tested |
| 2 | Register File | ✓ Implemented & Tested |
| 3 | Program Counter | ✓ Implemented & Tested |
| 4 | PC + 4 Adder | ✓ Implemented & Tested |
| 5 | Instruction Memory | ✓ Implemented & Tested |
| 6 | Instruction Decoder | ✓ Implemented & Tested |
| 7 | ALU Control | ✓ Implemented & Tested |
| 8 | Control Unit | ✓ Implemented & Tested |
| 9 | CPU Top | ✓ Implemented & Tested |

The current CPU top-level module wires together the PC, instruction memory, decoder, control logic, ALU control, register file, and ALU into a working single-cycle datapath model.

## RISC-V CPU Development Plan

| Step | Module | Status | Focus |
|------|--------|--------|--------------------------------------------------------------|
| 1 | ALU | ✓ | Combinational logic, always_comb, enums, case statements |
| 2 | Register File | ✓ | Arrays, synchronous writes, asynchronous reads |
| 3 | Program Counter | ✓ | Sequential logic, clocking, reset |
| 4 | PC + 4 Adder | ✓ | Simple combinational datapath |
| 5 | Instruction Memory | ✓ | ROM design, $readmemh |
| 6 | Instruction Decoder | ✓ | Bit slicing, instruction field extraction |
| 7 | ALU Control | ✓ | Decode logic, ALU operation selection |
| 8 | Control Unit | ✓ | Control signal generation |
| 9 | CPU Top | ✓ | Module integration and datapath wiring |
| 10 | I-Type Instructions | - | Immediate generation and execution |
| 11 | Branches and Jumps | - | Control-flow support |
| 12 | Pipeline | - | IF/ID, ID/EX, EX/MEM, MEM/WB pipeline stages |


           +----------------+
           |      PC        |
           +-------+--------+
                   |
                   v
           +----------------+
           | Instruction    |
           | Memory         |
           +-------+--------+
                   |
                   v
          +------------------+
          | Instruction      |
          | Decoder          |
          +--------+---------+
                   |
        +----------+-----------+
        |                      |
        v                      v
+---------------+      +----------------+
| Control Unit  |      | ALU Control    |
+-------+-------+      +--------+-------+
        |                       |
        |                       |
        v                       v
          +------------------+
          | Register File    |
          +--------+---------+
                   |
            rs1    |    rs2
                   v
              +---------+
              |   ALU   |
              +----+----+
                   |
                   |
                   +---------> Register File writeback