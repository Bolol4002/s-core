import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


async def reset(dut):
    dut.rst.value = 1

    # Hold reset for two cycles
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)

    dut.rst.value = 0


@cocotb.test()
async def test_cpu(dut):

    #
    # Start clock
    #
    cocotb.start_soon(
        Clock(dut.clk, 10, unit="ns").start()
    )

    #
    # Reset CPU
    #
    await reset(dut)

    #
    # Initialize the register file contents to avoid X-propagation.
    #
    for i in range(32):
        dut.u_regfile.mem[i].value = 0

    dut.u_regfile.mem[1].value = 10
    dut.u_regfile.mem[2].value = 20
    dut.u_regfile.mem[5].value = 0xFF
    dut.u_regfile.mem[12].value = 0x0F

    # Give the initial values a moment to settle.
    await Timer(1, unit="ns")

    #
    # Execute 4 instructions
    #
    for _ in range(4):
        await RisingEdge(dut.clk)

    #
    # Log the observed values before asserting.
    #
    dut._log.info(f"PC  = {hex(int(dut.u_pc.pc_o.value))}")
    dut._log.info(f"x3  = {hex(int(dut.u_regfile.mem[3].value))}")
    dut._log.info(f"x4  = {hex(int(dut.u_regfile.mem[4].value))}")
    dut._log.info(f"x5  = {hex(int(dut.u_regfile.mem[5].value))}")

    #
    # Check the architectural outputs.
    #
    dut.u_regfile.rs1_addr.value = 0
    await Timer(1, unit="ns")
    assert int(dut.u_regfile.rs1_data.value) == 0, (
        f"x0 should read as zero, got {int(dut.u_regfile.rs1_data.value)}"
    )

    assert int(dut.u_regfile.mem[3].value) == 30, \
        f"x3 incorrect: {int(dut.u_regfile.mem[3].value)}"

    assert int(dut.u_regfile.mem[4].value) == 10, \
        f"x4 incorrect: {int(dut.u_regfile.mem[4].value)}"

    assert int(dut.u_regfile.mem[5].value) == 0x0F, \
        f"x5 incorrect: {hex(int(dut.u_regfile.mem[5].value))}"

    dut._log.info("CPU integration test PASSED")