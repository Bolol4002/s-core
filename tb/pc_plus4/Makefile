# Makefile

SIM ?= icarus
TOPLEVEL_LANG ?= verilog
COMPILE_ARGS += -g2012
WAVES = 0

VERILOG_SOURCES += $(PWD)/../../src/pc_plus4.sv

TOPLEVEL = pc_plus4
MODULE = test_pc_plus4

include $(shell cocotb-config --makefiles)/Makefile.sim
