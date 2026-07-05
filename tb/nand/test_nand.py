import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_nand_gate(dut):
    """Verify NAND truth table."""

    test_vectors = [
        (0, 0, 1),
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 0),
    ]

    for a, b, expected in test_vectors:
        dut.a.value = a
        dut.b.value = b

        # Wait for combinational logic to settle
        await Timer(1, unit="ns")

        actual = int(dut.y.value)

        dut._log.info(
            f"a={a}, b={b}, y={actual}, expected={expected}"
        )

        assert actual == expected, (
            f"FAILED: a={a}, b={b}, expected={expected}, got={actual}"
        )
