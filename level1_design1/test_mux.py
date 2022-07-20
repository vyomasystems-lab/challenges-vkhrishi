# See LICENSE.vyoma for details
import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

   SEL= 5'b01100
   INP12=0

    # input driving
    dut.sel.value = SEL
    dut.inp12.value = INP12

    await Timer(2, units='ns')
    
    assert dut.out.value == , "Adder result is incorrect: {A} + {B} != {SUM}, expected value={EXP}".format(
            A=int(dut.a.value), B=int(dut.b.value), SUM=int(dut.sum.value), EXP=A+B)


@cocotb.test()
async def adder_randomised_test(dut):
    """Test for adding 2 random numbers multiple times"""

    for i in range(5):

        A = random.randint(0, 15)
        B = random.randint(0, 15)

        dut.a.value = A
        dut.b.value = B

        await Timer(2, units='ns')
        
        dut._log.info(f'A={A:05} B={B:05} model={A+B:05} DUT={int(dut.sum.value):05}')
        assert dut.sum.value == A+B, "Randomised test failed with: {A} + {B} = {SUM}".format(
            A=dut.a.value, B=dut.b.value, SUM=dut.sum.value)