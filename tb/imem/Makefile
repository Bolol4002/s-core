# Makefile

SIM ?= icarus
TOPLEVEL_LANG ?= verilog
COMPILE_ARGS += -g2012
WAVES = 0

VERILOG_SOURCES += $(PWD)/../../src/imem.sv

TOPLEVEL = imem
MODULE = test_imem

include $(shell cocotb-config --makefiles)/Makefile.sim
