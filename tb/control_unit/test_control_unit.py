import cocotb
from cocotb.triggers import Timer

R_TYPE = 0x33


@cocotb.test()
async def test_control_unit(dut):
    """Verify Control Unit decoding."""

    test_vectors = [
        # opcode, reg_write, alu_src, mem_read, mem_write,
        # mem_to_reg, branch, jump
        (R_TYPE, 1, 0, 0, 0, 0, 0, 0),
        (0x13,   1, 1, 0, 0, 0, 0, 0),
    ]

    for (
        opcode,
        reg_write,
        alu_src,
        mem_read,
        mem_write,
        mem_to_reg,
        branch,
        jump,
    ) in test_vectors:

        dut.opcode.value = opcode

        await Timer(1, units="ns")

        assert int(dut.reg_write.value) == reg_write
        assert int(dut.alu_src.value) == alu_src
        assert int(dut.mem_read.value) == mem_read
        assert int(dut.mem_write.value) == mem_write
        assert int(dut.mem_to_reg.value) == mem_to_reg
        assert int(dut.branch.value) == branch
        assert int(dut.jump.value) == jump

    cocotb.log.info("Control Unit test passed.")