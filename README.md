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
