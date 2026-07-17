import cocotb
from cocotb.triggers import Timer


R_TYPE = 0x33


@cocotb.test()
async def test_alu_control(dut):
    """Verify ALU Control decoding."""

    test_vectors = [
        # opcode, funct3, funct7, expected alu_op
        (R_TYPE, 0b000, 0b0000000, 0),  # ADD
        (R_TYPE, 0b000, 0b0100000, 1),  # SUB
        (R_TYPE, 0b111, 0b0000000, 2),  # AND
        (R_TYPE, 0b110, 0b0000000, 3),  # OR
        (0x13, 0b000, 0b0000000, 0),  # ADDI
        (0x13, 0b111, 0b0000000, 2),  # ANDI
        (0x13, 0b110, 0b0000000, 3),  # ORI
    ]

    for opcode, funct3, funct7, expected in test_vectors:

        dut.opcode.value = opcode
        dut.funct3.value = funct3
        dut.funct7.value = funct7

        await Timer(1, units="ns")

        actual = int(dut.alu_op.value)

        assert actual == expected, (
            f"opcode=0x{opcode:02X}, "
            f"funct3={funct3:03b}, "
            f"funct7={funct7:07b} "
            f"Expected={expected}, Got={actual}"
        )

    cocotb.log.info("ALU Control test passed.")