# Makefile

SIM ?= icarus
TOPLEVEL_LANG ?= verilog
COMPILE_ARGS += -g2012
WAVES = 0

VERILOG_SOURCES += $(PWD)/../../src/alu_control.sv

TOPLEVEL = alu_control
MODULE = test_alu_control

include $(shell cocotb-config --makefiles)/Makefile.sim
