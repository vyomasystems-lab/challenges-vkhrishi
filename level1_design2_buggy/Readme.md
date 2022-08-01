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
          next_state = IDLE;  ===>BUG1 
        else
          next_state = SEQ_10;
      end
      
SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = IDLE;  ===>BUG2
      end    
          
SEQ_1011:
      begin
        next_state = IDLE; ===>BUG3
      end          
          
      

```
For the Sequence Detector design, the logic should at SEQ_1 , SEQ101 , SEQ1011 should be 

```

SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = SEQ_10;
      end 
      
SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = SEQ_10;
      end
      
SEQ_1011:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = SEQ_10;
      end
      
```
      
instead of

```
SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = IDLE;  ===>BUG1 
        else
          next_state = SEQ_10;
      end
      
SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = IDLE;  ===>BUG2
      end    
          
SEQ_1011:
      begin
        next_state = IDLE; ===>BUG3
      end     
      
```

as in the design code.



## Design Fix
Updating the design and re-running the test makes the test pass.

![6](https://user-images.githubusercontent.com/59868949/181188504-8ee2a1fb-89bd-48ff-a5b6-e1c5e1ca5fd7.png)



The updated design is checked in level1_design2_fix


## Verification Strategy
Since the design was simple . So first I read verilog code .I drawn the state diagram for the given buggy code . I found error in logic of design , It was designed for non overlapping . After this is was easy to find the bugs using python testbench code.

## Is the verification complete ?
Yes the verification has completed . Just we have to change the logic of design to overlapping Moore design which is having n+1 states . Tested the code with different input sequence and found bugs to some of the sequences . By this I came to know that which state is not performing correctly . Finally tried to fix the bugs.
