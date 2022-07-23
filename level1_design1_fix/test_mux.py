# See LICENSE.vyoma for details
import cocotb
from cocotb.triggers import Timer
from random import randint


@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    

    for i in range(30):
       
       s=0b01100
       
    
       I0=0
       I1=1
       I2=2
       I3=3
       I4=0
       I5=1
       I6=2
       I7=3
       I8=0
       I9=1
       I10=2
       I11=3
       I12=3
       I13=2
       I14=1
       I15=0
       I16=0
       I17=1
       I18=2
       I19=3
       I20=0
       I21=1
       I22=2
       I23=3
       I24=0
       I25=1
       I26=2
       I27=3
       I28=0
       I29=1
       I30=2
       
       
       

       dut.sel.value = s
       dut.inp0.value = I0
       dut.inp1.value = I1
       dut.inp2.value = I2
       dut.inp3.value = I3
       dut.inp4.value = I4
       dut.inp5.value = I5
       dut.inp6.value = I6
       dut.inp7.value = I7
       dut.inp8.value = I8
       dut.inp9.value = I9
       dut.inp10.value = I10 
       dut.inp11.value = I11
       dut.inp12.value = I12
       dut.inp13.value = I13
       dut.inp14.value = I14
       dut.inp15.value = I15
       dut.inp16.value = I16
       dut.inp17.value = I17
       dut.inp18.value = I18
       dut.inp19.value = I19
       dut.inp20.value = I20
       dut.inp21.value = I21
       dut.inp22.value = I22
       dut.inp23.value = I23
       dut.inp24.value = I24
       dut.inp25.value = I25
       dut.inp26.value = I26
       dut.inp27.value = I27
       dut.inp28.value = I28
       dut.inp29.value = I29
       dut.inp30.value = I30
       d= int(s) 
       I=[0,1,2,3,0,1,2,3,0,1,2,3,3,2,1,0,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2]
       b = I[d]
       

       await Timer(2, units='ns')
        
       
       assert dut.out.value == b, "MUX result is incorrect:  {b} != {OUT}, expected value={EXP}".format(
          b=I[d],OUT=int(dut.out.value), EXP=I[d])
  