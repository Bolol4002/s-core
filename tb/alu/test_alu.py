import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_alu(dut):

    test_vectors = [
        (1, 1, 0, 2),   # ADD
        (2, 1, 1, 1),   # SUB
        (1, 1, 2, 1),   # AND
        (1, 0, 3, 1),   # OR
    ]

    for a, b, op, expected in test_vectors:

        dut.operand_a.value = a
        dut.operand_b.value = b
        dut.alu_op.value = op

        await Timer(1, units="ns")

        actual = int(dut.result.value)

        dut._log.info(
            f"op={op}, a={a}, b={b}, actual={actual}, expected={expected}"
        )

        assert actual == expected, (
            f"FAILED: op={op}, a={a}, b={b}, "
            f"actual={actual}, expected={expected}"
        )
