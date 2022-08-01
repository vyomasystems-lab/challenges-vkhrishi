# Bitmanipulation Coprocessor Design Verification

The verification environment is setup using Vyoma's UpTickPro provided for the hackathon.

![12](https://user-images.githubusercontent.com/59868949/181937684-de3dd144-797a-46d0-8231-da77aee8be00.png)


## Verification Environment
The CoCoTb based Python test is developed as explained. The test drives inputs to the Design Under Test (Bitmanipulation Coprocessor module here) which takes in 32 bit scr1 , scr2 , scr3 and 32 bit instruction.33 bit output in which one bit is reserved for validation .

The values are assigned to the input port using
```    
 mav_putvalue_src1 = random.randint(0,4294967295)
 mav_putvalue_src2 = random.randint(0,4294967295)
 mav_putvalue_src3 = random.randint(0,4294967295)
 mav_putvalue_instr = 0x401070B3
```       
 2 ^ 32 - 1 = 4294967295 
   
       
The assert statement is used for comparing the Bitmanipulation Coprocessor's output to the expected value.

The following error is seen:

![13](https://user-images.githubusercontent.com/59868949/181994548-5387ea5a-7257-40d5-a541-fe6e9cf54d2f.png)



Error 
```       
running run_test_ANDN_1 (1/58)
--ANDN 1
DUT OUTPUT=0x14a640
EXPECTED OUTPUT=0xcc841929
run_test_ANDN_1 failed
Traceback (most recent call last):
File "/workspace/challenges-vkhrishi/level2_design_buggy/test_mkbitmanip.py", line 62, in run_test_ANDN_1
assert dut_output == expected_mav_putvalue, error_message
AssertionError: Value mismatch DUT = 0x14a6405 does not match MODEL = 0xcc841929

```

                     
## Test Scenario  (Important)

- Test Inputs: mav_putvalue_src1 = random.randint(0,4294967295)
 mav_putvalue_src2 = random.randint(0,4294967295)
 mav_putvalue_src3 = random.randint(0,4294967295)
 mav_putvalue_instr = 0x401070B3 
- Expected Output: out=0xcc841929
- Observed Output in the DUT dut.out=0x14a640


Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following
```
if((func7 == "0100000") and (func3 == "111") and (opcode == "0110011") ):
        print('--ANDN 1')
        mav_putvalue=mav_putvalue_src1 & (~mav_putvalue_src2) ===>bug
        mav_putvalue=mav_putvalue & 0xffffffff
        mav_putvalue=(mav_putvalue<<1)|1
        return mav_putvalue
```
For the Bitmanipulation Coprocessor design, the logic should be ```mav_putvalue=mav_putvalue_src1 & (mav_putvalue_src2) ```instead of ``` mav_putvalue=mav_putvalue_src1 & (~mav_putvalue_src2)```as in the design code.



## Design Fix
Updating the design and re-running the test makes the test pass.


![14](https://user-images.githubusercontent.com/59868949/181994554-256fc4f3-ec78-4395-a2b5-655cdbfa0f64.png)


The updated design is checked in level2_design_fix


## Verification Strategy
First I read python model file which is having 58 different instruction . So I thought of checking bug in them . Giving random 32bit hex numbers to scr1,scr2,scr3
and 32 bit instruction (Total 58 instruction). Converted all the binary numbers to hex numbers to make it easy to read and write.

## Is the verification complete ?
I tried testing all 58 instruction by writing testbench code in python . Finally I found bug in ANDN instruction and also tried fixing the bug . 
