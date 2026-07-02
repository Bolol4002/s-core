import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def test_memory(dut):
    """Test byte-addressed word memory."""

    # ------------------------------------------------------------------
    # Start clock
    # ------------------------------------------------------------------
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

    # ------------------------------------------------------------------
    # Reset
    # ------------------------------------------------------------------
    dut.rst_n.value = 0
    dut.write_enable.value = 0
    dut.address.value = 0
    dut.write_data.value = 0

    # Hold reset for two clock cycles
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)

    dut.rst_n.value = 1
    await RisingEdge(dut.clk)

    # ------------------------------------------------------------------
    # After reset everything should be zero
    # ------------------------------------------------------------------
    for addr in [0, 4, 8, 12, 16]:
        dut.address.value = addr
        await Timer(1, units="ns")
        assert dut.read_data.value == 0, \
            f"Memory not cleared at address {addr}"

    # ------------------------------------------------------------------
    # Test aligned write
    # ------------------------------------------------------------------
    dut.address.value = 8          # Word index = 2
    dut.write_data.value = 0xDEADBEEF
    dut.write_enable.value = 1

    await RisingEdge(dut.clk)

    dut.write_enable.value = 0

    await Timer(1, units="ns")

    assert dut.read_data.value == 0xDEADBEEF, \
        "Aligned write failed"

    # ------------------------------------------------------------------
    # Test another aligned write
    # ------------------------------------------------------------------
    dut.address.value = 16         # Word index = 4
    dut.write_data.value = 0x12345678
    dut.write_enable.value = 1

    await RisingEdge(dut.clk)

    dut.write_enable.value = 0

    await Timer(1, units="ns")

    assert dut.read_data.value == 0x12345678, \
        "Second aligned write failed"

    # ------------------------------------------------------------------
    # Misaligned write should be ignored
    # ------------------------------------------------------------------
    dut.address.value = 5
    dut.write_data.value = 0xAAAAAAAA
    dut.write_enable.value = 1

    await RisingEdge(dut.clk)

    dut.write_enable.value = 0

    # Read word containing address 5
    dut.address.value = 4
    await Timer(1, units="ns")

    assert dut.read_data.value == 0, \
        "Misaligned write should have been ignored"

    # ------------------------------------------------------------------
    # Ensure previous writes still exist
    # ------------------------------------------------------------------
    dut.address.value = 8
    await Timer(1, units="ns")

    assert dut.read_data.value == 0xDEADBEEF

    dut.address.value = 16
    await Timer(1, units="ns")

    assert dut.read_data.value == 0x12345678

    dut._log.info("All memory tests passed.")
