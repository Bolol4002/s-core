# Makefile

SIM ?= icarus
TOPLEVEL_LANG ?= verilog
COMPILE_ARGS += -g2012
WAVES = 0

VERILOG_SOURCES += $(PWD)/../../src/dmem.sv

TOPLEVEL = dmem
MODULE = test_dmem

include $(shell cocotb-config --makefiles)/Makefile.sim
