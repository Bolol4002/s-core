import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


async def reset_inputs(dut):
    dut.we.value = 0
    dut.rs1_addr.value = 0
    dut.rs2_addr.value = 0
    dut.rd_addr.value = 0
    dut.rd_data.value = 0
    await Timer(1, unit="ns")


async def write_reg(dut, addr, value):
    dut.we.value = 1
    dut.rd_addr.value = addr
    dut.rd_data.value = value

    await RisingEdge(dut.clk)

    dut.we.value = 0


@cocotb.test()
async def test_regfile(dut):

    # clock
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())

    await reset_inputs(dut)

    golden = [0] * 32

    # -------------------------
    # x0 should always be zero
    # -------------------------
    dut.rs1_addr.value = 0
    dut.rs2_addr.value = 0
    await Timer(1, unit="ns")

    assert int(dut.rs1_data.value) == 0
    assert int(dut.rs2_data.value) == 0

    # -------------------------
    # Write x5 = 0x12345678
    # -------------------------
    await write_reg(dut, 5, 0x12345678)
    golden[5] = 0x12345678

    dut.rs1_addr.value = 5
    await Timer(1, unit="ns")
    assert int(dut.rs1_data.value) == 0x12345678

    # -------------------------
    # Write disabled check
    # -------------------------
    await write_reg(dut, 6, 0)

    dut.we.value = 0
    dut.rd_addr.value = 6
    dut.rd_data.value = 0xDEADBEEF
    await RisingEdge(dut.clk)

    dut.rs2_addr.value = 6
    await Timer(1, unit="ns")
    assert int(dut.rs2_data.value) == 0

    # -------------------------
    # x0 write protection
    # -------------------------
    await write_reg(dut, 0, 0xFFFFFFFF)

    dut.rs1_addr.value = 0
    await Timer(1, unit="ns")
    assert int(dut.rs1_data.value) == 0

    # -------------------------
    # Full register write test
    # -------------------------
    for reg in range(1, 32):
        val = reg * 100
        await write_reg(dut, reg, val)
        golden[reg] = val

    # -------------------------
    # Dual-read verification
    # -------------------------
    for r1 in range(32):
        for r2 in range(32):

            dut.rs1_addr.value = r1
            dut.rs2_addr.value = r2

            await Timer(1, unit="ns")

            assert int(dut.rs1_data.value) == golden[r1], \
                f"rs1 mismatch reg={r1}"

            assert int(dut.rs2_data.value) == golden[r2], \
                f"rs2 mismatch reg={r2}"

    # -------------------------
    # final x0 check
    # -------------------------
    dut.rs1_addr.value = 0
    dut.rs2_addr.value = 0

    await Timer(1, unit="ns")

    assert int(dut.rs1_data.value) == 0
    assert int(dut.rs2_data.value) == 0

    dut._log.info("REGISTER FILE TEST PASSED")
