# Makefile

SIM ?= icarus
TOPLEVEL_LANG ?= verilog
COMPILE_ARGS += -g2012
WAVES = 0

VERILOG_SOURCES += $(PWD)/../../src/imm_gen.sv

TOPLEVEL = imm_gen
MODULE = test_imm_gen

include $(shell cocotb-config --makefiles)/Makefile.sim
