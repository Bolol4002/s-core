import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_instruction_memory(dut):
    """Verify instruction ROM contents."""

    test_vectors = [
        (0x00000000, 0x002081B3),
        (0x00000004, 0x40110233),
        (0x00000008, 0x00C2F2B3),
        (0x0000000C, 0x00000013),
    ]

    for addr, expected in test_vectors:
        dut.addr.value = addr

        # Allow combinational logic to settle
        await Timer(1, units="ns")

        actual = int(dut.instruction.value)

        assert actual == expected, (
            f"Address 0x{addr:08X}: "
            f"Expected 0x{expected:08X}, "
            f"Got 0x{actual:08X}"
        )

    cocotb.log.info("Instruction memory test passed.")