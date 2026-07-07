# Makefile

SIM ?= icarus
TOPLEVEL_LANG ?= verilog
COMPILE_ARGS += -g2012
WAVES = 0

VERILOG_SOURCES += $(PWD)/../../src/pc.sv

TOPLEVEL = pc
MODULE = test_pc

include $(shell cocotb-config --makefiles)/Makefile.sim
