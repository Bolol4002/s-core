# Makefile

SIM ?= icarus
TOPLEVEL_LANG ?= verilog
COMPILE_ARGS += -g2012
WAVES = 0

VERILOG_SOURCES += $(PWD)/../../src/alu.sv

TOPLEVEL = alu
MODULE = test_alu

include $(shell cocotb-config --makefiles)/Makefile.sim
