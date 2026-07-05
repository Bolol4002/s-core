#!/usr/bin/env bash
set -e

read -p "Enter module name: " name

if [ -z "$name" ]; then
  echo "Error: no name provided"
  exit 1
fi

# Create src/<name>.sv
cat > "src/${name}.sv" <<EOF
module ${name}(input a, input b, output y);
   assign y = ~(a & b);
endmodule
EOF

# Create tb/<name>/ directory and files
mkdir -p "tb/${name}"

cat > "tb/${name}/test_${name}.py" <<EOF
import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_${name}(dut):
    """Verify ${name} truth table."""

    test_vectors = [
        (0, 0, 1),
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 0),
    ]

    for a, b, expected in test_vectors:
        dut.a.value = a
        dut.b.value = b
        await Timer(1, unit="ns")
        actual = int(dut.y.value)
        dut._log.info(f"a={a}, b={b}, y={actual}, expected={expected}")
        assert actual == expected, f"FAILED: a={a}, b={b}, expected={expected}, got={actual}"
EOF

cat > "tb/${name}/Makefile" <<EOF
# Makefile

SIM ?= icarus
TOPLEVEL_LANG ?= verilog
COMPILE_ARGS += -g2012
WAVES = 0

VERILOG_SOURCES += \$(PWD)/../../src/${name}.sv

TOPLEVEL = ${name}
MODULE = test_${name}

include \$(shell cocotb-config --makefiles)/Makefile.sim
EOF

echo ""
echo "Created:"
echo "  src/${name}.sv"
echo "  tb/${name}/test_${name}.py"
echo "  tb/${name}/Makefile"
echo ""
echo "Run: cd tb/${name} && make"
