# See LICENSE.iitm for details
# See LICENSE.vyoma for details

import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock


# Clock Generation
@cocotb.coroutine
def clock_gen(signal):
    while True:
        signal.value <= 0
        yield Timer(1) 
        signal.value <= 1
        yield Timer(1) 

# Sample Test
@cocotb.test()
def run_test(dut):

    # clock
    cocotb.fork(clock_gen(dut.clk))

    # reset
    dut.rst.value <= 0
    yield Timer(10) 
    dut.rst.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    count = 5

    # expected output from the model
    expected_light_M1 = 0b001
    expected_light_M2 = 0b001
    expected_light_MT = 0b100
    expected_light_S = 0b100

    # driving the input transaction
    dut.count.value = count
  
    yield Timer(10) 

    # obtaining the output
    dut_output_light_M1 = dut.light_M1.value
    dut_output_light_M2 = dut.light_M2.value
    dut_output_light_MT = dut.light_MT.value
    dut_output_light_S  = dut.light_S.value
    cocotb.log.info(f'DUT OUTPUT={bin(dut_output_light_M1)}')
    cocotb.log.info(f'EXPECTED OUTPUT={bin(expected_light_M1)}')
    cocotb.log.info(f'DUT OUTPUT={bin(dut_output_light_M2)}')
    cocotb.log.info(f'EXPECTED OUTPUT={bin(expected_light_M2)}')
    cocotb.log.info(f'DUT OUTPUT={bin(dut_output_light_MT)}')
    cocotb.log.info(f'EXPECTED OUTPUT={bin(expected_light_MT)}')
    cocotb.log.info(f'DUT OUTPUT={bin(dut_output_light_S)}')
    cocotb.log.info(f'EXPECTED OUTPUT={bin(expected_light_S)}')
    
    # comparison
    error_message = f'Value mismatch DUT = {bin(dut_output_light_M1)} does not match MODEL = {bin(expected_light_M1)}'
    assert dut_output_light_M1 == expected_light_M1, error_message
    error_message = f'Value mismatch DUT = {bin(dut_output_light_M2)} does not match MODEL = {bin(expected_light_M2)}'
    assert dut_output_light_M2 == expected_light_M2, error_message
    error_message = f'Value mismatch DUT = {bin(dut_output_light_MT)} does not match MODEL = {bin(expected_light_MT)}'
    assert dut_output_light_MT == expected_light_MT, error_message
    error_message = f'Value mismatch DUT = {bin(dut_output_light_S)} does not match MODEL = {bin(expected_light_S)}'
    assert dut_output_light_S == expected_light_S, error_message