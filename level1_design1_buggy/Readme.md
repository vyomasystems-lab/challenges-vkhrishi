# Multiplexer Design Verification

The verification environment is setup using Vyoma's UpTickPro provided for the hackathon.

![WhatsApp Image 2022-07-22 at 20 52 00](https://user-images.githubusercontent.com/59868949/180484987-54c6ee00-6970-46dc-855d-f854fb6fd6e1.jpeg)

## Verification Environment
The CoCoTb based Python test is developed as explained. The test drives inputs to the Design Under Test (Multiplexer module here) which takes in 5-bit input Select line
,2-bit 0-30 input ports and gives 2-bit output known as 31x1 Multiplexer.

The values are assigned to the input port using
```    
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
```       
       
       
The assert statement is used for comparing the Multiplexer's output to the expected value.

The following error is seen:
```       
assert dut.out.value == b, "MUX result is incorrect:  {b} != {OUT}, expected value={EXP}".format(AssertionError: MUX result is incorrect:  3 != 0, expected value=3
```
## Test Scenario (Important)
- Test Inputs: sel=0b01100,inp12=3
- Expected Output: out=3
- Observed Output in the DUT dut.out=0

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following
```
5'b01011: out = inp11;
5'b01101: out = inp12;  ===> BUG
5'b01101: out = inp13;
```
For the adder design, the logic should be ```5'b01100: out = inp12; ```instead of ``` 5'b01101: out = inp12;```as in the design code.

## Design Fix
Updating the design and re-running the test makes the test pass.

![1](https://user-images.githubusercontent.com/59868949/180506416-3bfd448c-f222-4e5d-a554-cb1f702675b2.png)

The updated design is checked in as adder_fix.v







