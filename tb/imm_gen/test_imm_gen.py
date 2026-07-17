import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_imm_gen(dut):
    """Verify sign extension for I-type immediates."""

    test_vectors = [
        (0x00A00093, 10),
        (0xFFC00093, 0xFFFFFFFC),
    ]

    for instruction, expected in test_vectors:
        dut.instruction.value = instruction

        await Timer(1, units="ns")

        actual = int(dut.imm.value)
        assert actual == expected, (
            f"instruction=0x{instruction:08X}, expected=0x{expected:08X}, got=0x{actual:08X}"
        )

    cocotb.log.info("Immediate Generator test passed.")
