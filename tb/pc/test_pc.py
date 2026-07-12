import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


async def wait_for_update():
    """Allow one simulation timestep for nonblocking assignments to settle."""
    await Timer(1, unit="ns")


@cocotb.test()
async def test_pc(dut):
    """Test the Program Counter module."""

    # Start 10 ns clock
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())

    # Initialize
    dut.rst.value = 1
    dut.next_pc.value = 0

    await Timer(1, unit="ns")

    # Apply reset
    await RisingEdge(dut.clk)
    await wait_for_update()
    assert dut.pc_o.value == 0, f"Expected PC = 0, got {dut.pc_o.value}"

    await RisingEdge(dut.clk)
    await wait_for_update()
    assert dut.pc_o.value == 0, f"Expected PC = 0, got {dut.pc_o.value}"

    # Release reset
    dut.rst.value = 0
    await wait_for_update()

    # Test 1
    dut.next_pc.value = 0x4
    await wait_for_update()
    await RisingEdge(dut.clk)
    await wait_for_update()
    assert dut.pc_o.value == 0x4, \
        f"Expected 0x4, got {hex(int(dut.pc_o.value))}"

    # Test 2
    dut.next_pc.value = 0x8
    await wait_for_update()
    await RisingEdge(dut.clk)
    await wait_for_update()
    assert dut.pc_o.value == 0x8, \
        f"Expected 0x8, got {hex(int(dut.pc_o.value))}"

    # Test 3
    dut.next_pc.value = 0xC
    await wait_for_update()
    await RisingEdge(dut.clk)
    await wait_for_update()
    assert dut.pc_o.value == 0xC, \
        f"Expected 0xC, got {hex(int(dut.pc_o.value))}"

    # Assert reset again
    dut.rst.value = 1
    await wait_for_update()
    await RisingEdge(dut.clk)
    await wait_for_update()
    assert dut.pc_o.value == 0, \
        f"Expected 0 after reset, got {hex(int(dut.pc_o.value))}"

    # Release reset
    dut.rst.value = 0
    await wait_for_update()

    # Test 4
    dut.next_pc.value = 0x10
    await wait_for_update()
    await RisingEdge(dut.clk)
    await wait_for_update()
    assert dut.pc_o.value == 0x10, \
        f"Expected 0x10, got {hex(int(dut.pc_o.value))}"

    dut._log.info("All PC tests passed.")