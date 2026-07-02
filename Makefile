TOPLEVEL_LANG ?= verilog
SIM ?= verilator

ifeq (,$(TOPLEVEL))

# ------------------------------------------------------------------
# Dispatch mode – user runs 'make <name>'
# ------------------------------------------------------------------
.PHONY: help clean

help:
	@echo "Usage: make <name>"
	@echo ""
	@echo "Available targets:"
	@ls src/*.sv 2>/dev/null | sed 's|src/\(.*\)\.sv|  \1|'

clean:
	rm -rf sim_build results.xml
	rm -f *.vcd

%: src/%.sv tb/%.py
	$(MAKE) TOPLEVEL=$@ \
	       VERILOG_SOURCES="$(PWD)/src/$@.sv" \
	       MODULE=tb.$@ \
	       SIM_BUILD=$(PWD)/sim_build/$@ \
	       PYTHONPATH="$(PWD)"

else

# ------------------------------------------------------------------
# Build mode – Cocotb + Verilator
# ------------------------------------------------------------------
COCOTB_MAKEFILES := $(shell cocotb-config --makefiles)

export PYTHONPATH

include $(COCOTB_MAKEFILES)/Makefile.sim

endif
