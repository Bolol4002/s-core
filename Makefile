TOPLEVEL_LANG ?= verilog
PATH := $(PWD)/venv/bin:$(PATH)
SIM ?= $(shell \
    if command -v verilator >/dev/null 2>&1; then \
        v=$$(verilator --version 2>/dev/null | awk '{print $$2}'); \
        if [ "$$(printf '%s\n' 5.036 "$$v" | sort -V | head -n1)" = "5.036" ]; then \
            echo verilator; \
        elif command -v iverilog >/dev/null 2>&1; then \
            echo icarus; \
        else \
            echo verilator; \
        fi; \
    elif command -v iverilog >/dev/null 2>&1; then \
        echo icarus; \
    fi)

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
export PYTHONPATH
export PATH := $(PWD)/venv/bin:$(PATH)

COCOTB_CONFIG ?= $(shell command -v cocotb-config 2>/dev/null)
ifeq ($(COCOTB_CONFIG),)
$(error cocotb-config not found. Activate the repository virtualenv with 'source venv/bin/activate' or install cocotb.)
endif

COCOTB_MAKEFILES := $(shell $(COCOTB_CONFIG) --makefiles)
include $(COCOTB_MAKEFILES)/Makefile.sim

endif
