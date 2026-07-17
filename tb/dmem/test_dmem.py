import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def test_dmem(dut):
    """Verify basic synchronous write and asynchronous read behavior."""

    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())

    address = 0x100
    data = 0xDEADBEEF

    dut.mem_write.value = 1
    dut.mem_read.value = 0
    dut.addr.value = address
    dut.write_data.value = data

    await RisingEdge(dut.clk)

    dut.mem_write.value = 0
    dut.mem_read.value = 1
    dut.addr.value = address

    await Timer(1, unit="ns")

    actual = int(dut.read_data.value)
    assert actual == data, f"expected 0x{data:08X}, got 0x{actual:08X}"

    cocotb.log.info("Data memory test passed.")
