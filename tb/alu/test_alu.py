import random
import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_alu_random(dut):

    NUM_TESTS = 20

    for i in range(NUM_TESTS):

        # Random inputs
        a = random.randint(0, 0xFFFFFFFF)
        b = random.randint(0, 0xFFFFFFFF)
        op = random.randint(0, 3)

        # Drive DUT
        dut.operand_a.value = a
        dut.operand_b.value = b
        dut.alu_op.value = op

        await Timer(1, unit="ns")

        # ---------- Golden Model ----------
        if op == 0:          # ADD
            expected = (a + b) & 0xFFFFFFFF

        elif op == 1:        # SUB
            expected = (a - b) & 0xFFFFFFFF

        elif op == 2:        # AND
            expected = a & b

        elif op == 3:        # OR
            expected = a | b

        expected_zero = int(expected == 0)

        # ---------- Read DUT ----------
        actual = int(dut.result.value)
        actual_zero = int(dut.zero.value)

        # ---------- Logging ----------
        dut._log.info(
            f"Test {i:04d}: "
            f"op={op} "
            f"a=0x{a:08X} "
            f"b=0x{b:08X} "
            f"expected=0x{expected:08X} "
            f"actual=0x{actual:08X}"
        )

        # ---------- Check Result ----------
        assert actual == expected, (
            f"\n"
            f"Test #{i}\n"
            f"Operation : {op}\n"
            f"A         : 0x{a:08X}\n"
            f"B         : 0x{b:08X}\n"
            f"Expected  : 0x{expected:08X}\n"
            f"Actual    : 0x{actual:08X}"
        )

        # ---------- Check Zero Flag ----------
        assert actual_zero == expected_zero, (
            f"\n"
            f"Zero flag mismatch\n"
            f"Result        : 0x{expected:08X}\n"
            f"Expected Zero : {expected_zero}\n"
            f"Actual Zero   : {actual_zero}"
        )
