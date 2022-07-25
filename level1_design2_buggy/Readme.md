# 1011 Sequence Detector Design Verification

The verification environment is setup using Vyoma's UpTickPro provided for the hackathon.

![4](https://user-images.githubusercontent.com/59868949/180657296-181a5752-32bf-4d20-9ac7-874928febd9e.png)


## Verification Environment
The CoCoTb based Python test is developed as explained. The test drives inputs to the Design Under Test (Sequence Detector module here) which takes in 1-bit input and 1-bit output.

The values are assigned to the input port using
```
####Test1

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
    
####Test2
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
    
####Test3  
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
    
    

      
```               
       
The assert statement is used for comparing the Sequence Detector's output to the expected value.

The following error is seen:

![5](https://user-images.githubusercontent.com/59868949/180848768-1009059d-e862-4739-b203-ba1221b97c99.png)

Error 1 when input sequence is 
```       
assert dut.seq_seen.value == b, "Sequence given 11011, result is incorrect:  {b} != {OUT}, expected value={EXP}".format(
 AssertionError: Sequence given 11011, result is incorrect:  1 != 0, expected value=1
```
Error 2 when input sequence is
```
 assert dut.seq_seen.value == b, "Sequence given 111011, result is incorrect:  {b} != {OUT}, expected value={EXP}".format(
 AssertionError: Sequence given 111011, result is incorrect:  1 != 0, expected value=1
``` 
Error 3 when input sequence is
```
assert dut.seq_seen.value == b, "Sequence given 1011011, result is incorrect:  {b} != {OUT}, expected value={EXP}".format(
AssertionError: Sequence given 1011011, result is incorrect:  1 != 0, expected value=1
```
                     
## Test Scenario  (Important)
### 1
- Test Inputs: int_bit sequence 11011
- Expected Output: out=1
- Observed Output in the DUT dut.out=0
### 2
- Test Inputs: int_bit sequence 111011
- Expected Output: out=1
- Observed Output in the DUT dut.out=0
### 3
- Test Inputs: int_bit sequence 1011011 
- Expected Output: out=1
- Observed Output in the DUT dut.out=0

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following
```
SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = IDLE;  ===>BUG 
        else
          next_state = SEQ_10;
      end

```
For the Multiplexer design, the logic should be ```5'b01100: out = inp12; ```instead of ``` 5'b01101: out = inp12;```as in the design code.

```5'b11110: out = inp30;``` is missing in this logic.

## Design Fix
Updating the design and re-running the test makes the test pass.


![3](https://user-images.githubusercontent.com/59868949/180653626-ba12fba5-8903-4bb0-be6f-6d5b0219c1cb.png)

The updated design is checked in level1_design1_fix

