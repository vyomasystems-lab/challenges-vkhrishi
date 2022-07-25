# See LICENSE.vyoma for details
 
# SPDX-License-Identifier: CC0-1.0
 
import os
import random
from pathlib import Path
 
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer
 
@cocotb.test()
async def test1_seq_bug1(dut):
    """Test for seq detection """
 
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
 
    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)
 
    cocotb.log.info('#### CTB: Develop your test here! ######')
 
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    
    b=1
    
    dut._log.info(f'b={b:02} model={b:02} DUT={int(dut.seq_seen.value):02}')
    assert dut.seq_seen.value == b, "Sequence given 11011, result is incorrect:  {b} != {OUT}, expected value={EXP}".format(
       b=1, OUT=int(dut.seq_seen.value), EXP=b)


@cocotb.test()
async def test2_seq_bug2(dut):
    """Test for seq detection """
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
 
     
    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)
    dut.reset.value = 0
    await FallingEdge(dut.clk)
 
    cocotb.log.info('#### CTB: Develop your test here! ######')
 
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
  
 
 
    b=1
    
    dut._log.info(f'b={b:02} model={b:02} DUT={int(dut.seq_seen.value):02}')
    assert dut.seq_seen.value == b, "Sequence given 111011, result is incorrect:  {b} != {OUT}, expected value={EXP}".format(
       b=1, OUT=int(dut.seq_seen.value), EXP=b)

@cocotb.test()
async def test3_seq_bug3(dut):
    """Test for seq detection """
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
 
     
    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)
    dut.reset.value = 0
    await FallingEdge(dut.clk)
 
    cocotb.log.info('#### CTB: Develop your test here! ######')
 
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk)
 
 
    b=1
    
    dut._log.info(f'b={b:02} model={b:02} DUT={int(dut.seq_seen.value):02}')
    assert dut.seq_seen.value == b, "Sequence given 1011011, result is incorrect:  {b} != {OUT}, expected value={EXP}".format(
       b=1, OUT=int(dut.seq_seen.value), EXP=b)       