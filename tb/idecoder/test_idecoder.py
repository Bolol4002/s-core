import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_instruction_decoder(dut):
    """Verify instruction field extraction."""

    test_vectors = [
        {
            "instruction": 0x002081B3,  # add x3, x1, x2
            "opcode": 0x33,
            "rd": 3,
            "funct3": 0x0,
            "rs1": 1,
            "rs2": 2,
            "funct7": 0x00,
        },
        {
            "instruction": 0x40110233,  # sub x4, x2, x1
            "opcode": 0x33,
            "rd": 4,
            "funct3": 0x0,
            "rs1": 2,
            "rs2": 1,
            "funct7": 0x20,
        },
        {
            "instruction": 0x00C2F2B3,  # and x5, x5, x12
            "opcode": 0x33,
            "rd": 5,
            "funct3": 0x7,
            "rs1": 5,
            "rs2": 12,
            "funct7": 0x00,
        },
    ]

    for tv in test_vectors:
        dut.instruction.value = tv["instruction"]

        # Allow combinational outputs to settle
        await Timer(1, units="ns")

        assert int(dut.opcode.value) == tv["opcode"], \
            f"Opcode mismatch for 0x{tv['instruction']:08X}"

        assert int(dut.rd.value) == tv["rd"], \
            f"RD mismatch for 0x{tv['instruction']:08X}"

        assert int(dut.funct3.value) == tv["funct3"], \
            f"funct3 mismatch for 0x{tv['instruction']:08X}"

        assert int(dut.rs1.value) == tv["rs1"], \
            f"RS1 mismatch for 0x{tv['instruction']:08X}"

        assert int(dut.rs2.value) == tv["rs2"], \
            f"RS2 mismatch for 0x{tv['instruction']:08X}"

        assert int(dut.funct7.value) == tv["funct7"], \
            f"funct7 mismatch for 0x{tv['instruction']:08X}"

    cocotb.log.info("Instruction decoder test passed.")