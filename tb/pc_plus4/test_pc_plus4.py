import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_pc_plus4(dut):
    """Verify pc_plus4 truth table."""

    bank = [
    (0x00000000, 0x00000004),
    (0x00000004, 0x00000008),
    (0x00000100, 0x00000104),
    (0x7FFFFFFC, 0x80000000),
    (0xFFFFFFFC, 0x00000000),
    ]

    for a,expected in bank:
        dut.pc_i.value = a
        await Timer(1, unit="ns")
        actual = int(dut.next_pc.value)
        #dut._log.info(f"a={a}, b={b}, y={actual}, expected={expected}")
        assert actual == expected, f"FAILED: a={a}, b={b}, expected={expected}, got={actual}"
