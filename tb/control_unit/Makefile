# Makefile

SIM ?= icarus
TOPLEVEL_LANG ?= verilog
COMPILE_ARGS += -g2012
WAVES = 0

VERILOG_SOURCES += $(PWD)/../../src/control_unit.sv

TOPLEVEL = control_unit
MODULE = test_control_unit

include $(shell cocotb-config --makefiles)/Makefile.sim
