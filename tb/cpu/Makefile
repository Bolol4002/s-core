# Makefile

SIM ?= icarus
TOPLEVEL_LANG ?= verilog
COMPILE_ARGS += -g2012
WAVES = 0

VERILOG_SOURCES += $(PWD)/../../src/cpu_pkg.sv
VERILOG_SOURCES += $(PWD)/../../src/pc.sv
VERILOG_SOURCES += $(PWD)/../../src/pc_plus4.sv
VERILOG_SOURCES += $(PWD)/../../src/imem.sv
VERILOG_SOURCES += $(PWD)/../../src/idecoder.sv
VERILOG_SOURCES += $(PWD)/../../src/control_unit.sv
VERILOG_SOURCES += $(PWD)/../../src/alu_control.sv
VERILOG_SOURCES += $(PWD)/../../src/regfile.sv
VERILOG_SOURCES += $(PWD)/../../src/alu.sv
VERILOG_SOURCES += $(PWD)/../../src/cpu.sv

TOPLEVEL = cpu
MODULE = test_cpu

include $(shell cocotb-config --makefiles)/Makefile.sim
