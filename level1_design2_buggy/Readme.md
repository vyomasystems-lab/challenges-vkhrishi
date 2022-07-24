# Sequence Detector Design Verification

The verification environment is setup using Vyoma's UpTickPro provided for the hackathon.

![4](https://user-images.githubusercontent.com/59868949/180657296-181a5752-32bf-4d20-9ac7-874928febd9e.png)


## Verification Environment
The CoCoTb based Python test is developed as explained. The test drives inputs to the Design Under Test (Multiplexer module here) which takes in 5-bit input Select line,2-bit 0-30 input ports and gives 2-bit output known as 31x1 Multiplexer.

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
When``` s=0b01100,
        s=0b01101,
        s=0b11110,
        dut.sel.value=s```        
       
The assert statement is used for comparing the Multiplexer's output to the expected value.

The following error is seen:

![2](https://user-images.githubusercontent.com/59868949/180653622-def72a01-cd7f-4dec-9793-fa2782c38c89.png)

Error 1 when s=0b01100
```       
assert dut.out.value == b, "MUX result is incorrect:  {b} != {OUT}, expected value={EXP}".format(
AssertionError: MUX result is incorrect:  3 != 0, expected value=3
```
Error 2 when s=0b01101
```
assert dut.out.value == b, "MUX result is incorrect:  {b} != {OUT}, expected value={EXP}".format(
AssertionError: MUX result is incorrect:  2 != 3, expected value=2
``` 
Error 3 when s=0b11110
```
assert dut.out.value == b, "MUX result is incorrect:  {b} != {OUT}, expected value={EXP}".format(
AssertionError: MUX result is incorrect:  2 != 0, expected value=2
```
                     
## Test Scenario  (Important)
### 1
- Test Inputs: sel=0b01100,inp12=3
- Expected Output: out=3
- Observed Output in the DUT dut.out=0
### 2
- Test Inputs: sel=0b01101,inp13=2
- Expected Output: out=2
- Observed Output in the DUT dut.out=3
### 3
- Test Inputs: sel=0b11110,inp30=2
- Expected Output: out=2
- Observed Output in the DUT dut.out=0

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following
```
5'b01011: out = inp11;
5'b01101: out = inp12;  ===> BUG at inp12 and inp13
5'b01101: out = inp13;  
.
.
.
 5'b11100: out = inp28;
 5'b11101: out = inp29;
                        ===>BUG inp30 missing
 default: out = 0;
```
For the Multiplexer design, the logic should be ```5'b01100: out = inp12; ```instead of ``` 5'b01101: out = inp12;```as in the design code.

```5'b11110: out = inp30;``` is missing in this logic.

## Design Fix
Updating the design and re-running the test makes the test pass.


![3](https://user-images.githubusercontent.com/59868949/180653626-ba12fba5-8903-4bb0-be6f-6d5b0219c1cb.png)

The updated design is checked in level1_design1_fix

