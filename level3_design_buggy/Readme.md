# Traffic Light Controller Design Verification

The verification environment is setup using Vyoma's UpTickPro provided for the hackathon.

![12](https://user-images.githubusercontent.com/59868949/182022760-31ea034e-b5d6-4276-9676-12b12bf4f5c4.png)


## Verification Environment
The CoCoTb based Python test is developed as explained. The test drives inputs to the Design Under Test (Traffic Light Controller module here) which takes in 5bit input and four 3bit RYG (red , yellow , green) output named light_M1 , light_M2 , light_MT , light_S.

The values are assigned to the input port using
``` 
#1
    NO_of_vehical = 7
    expected_light_M1 = 0b001
    expected_light_M2 = 0b001
    expected_light_MT = 0b100
    expected_light_S = 0b100
    
    dut.NO_of_vehical.value = NO_of_vehical
    dut_output_light_M1 = dut.light_M1.value
    dut_output_light_M2 = dut.light_M2.value
    dut_output_light_MT = dut.light_MT.value
    dut_output_light_S  = dut.light_S.value
#2
    
    NO_of_vehical = 2
    expected_light_M1 = 0b001
    expected_light_M2 = 0b010
    expected_light_MT = 0b100
    expected_light_S = 0b100
    
    dut.NO_of_vehical.value = NO_of_vehical
    dut_output_light_M1 = dut.light_M1.value
    dut_output_light_M2 = dut.light_M2.value
    dut_output_light_MT = dut.light_MT.value
    dut_output_light_S  = dut.light_S.value
    
#3
    
    NO_of_vehical = 5
    expected_light_M1 = 0b001
    expected_light_M2 = 0b100
    expected_light_MT = 0b001
    expected_light_S = 0b100

    dut.NO_of_vehical.value = NO_of_vehical
    dut_output_light_M1 = dut.light_M1.value
    dut_output_light_M2 = dut.light_M2.value
    dut_output_light_MT = dut.light_MT.value
    dut_output_light_S  = dut.light_S.value
    
#4
    
    NO_of_vehical = 4
    expected_light_M1 = 0b010
    expected_light_M2 = 0b100
    expected_light_MT = 0b010
    expected_light_S = 0b100 
    
    dut.NO_of_vehical.value = NO_of_vehical
    dut_output_light_M1 = dut.light_M1.value
    dut_output_light_M2 = dut.light_M2.value
    dut_output_light_MT = dut.light_MT.value
    dut_output_light_S  = dut.light_S.value
    
#5
   
    NO_of_vehical = 3
    expected_light_M1 = 0b100
    expected_light_M2 = 0b100
    expected_light_MT = 0b100
    expected_light_S = 0b001

    dut.NO_of_vehical.value = NO_of_vehical
    dut_output_light_M1 = dut.light_M1.value
    dut_output_light_M2 = dut.light_M2.value
    dut_output_light_MT = dut.light_MT.value
    dut_output_light_S  = dut.light_S.value
    
#6

    NO_of_vehical = 6
    expected_light_M1 = 0b100
    expected_light_M2 = 0b100
    expected_light_MT = 0b100
    expected_light_S = 0b010
    
    dut.NO_of_vehical.value = NO_of_vehical
    dut_output_light_M1 = dut.light_M1.value
    dut_output_light_M2 = dut.light_M2.value
    dut_output_light_MT = dut.light_MT.value
    dut_output_light_S  = dut.light_S.value
    
       
```       
        
       
The assert statement is used for comparing the Traffic Light Controller's output to the expected value.

The following error is seen:

![8](https://user-images.githubusercontent.com/59868949/182023212-8c0f77fa-1992-4ee7-8b3e-c3390493302f.png)

Error 1 when No_of_vehical = 7
``` 
running run_test1 (1/6)
     0.02ns INFO     DUT OUTPUT=0b1
     0.02ns INFO     EXPECTED OUTPUT=0b1
     0.02ns INFO     DUT OUTPUT=0b101
     0.02ns INFO     EXPECTED OUTPUT=0b1
     0.02ns INFO     DUT OUTPUT=0b100
     0.02ns INFO     EXPECTED OUTPUT=0b100
     0.02ns INFO     DUT OUTPUT=0b100
     0.02ns INFO     EXPECTED OUTPUT=0b100
     0.02ns INFO     run_test1 failed
                     Traceback (most recent call last):
                       File "/workspace/challenges-vkhrishi/level3_design_buggy/test.py", line 68, in run_test1
                         assert dut_output_light_M2 == expected_light_M2, error_message
                     AssertionError: Value mismatch DUT = 0b101 does not match MODEL = 0b1

```
Error 2 when No_of_vehical = 2
```
 0.02ns INFO     running run_test2 (2/6)
     0.04ns INFO     DUT OUTPUT=0b1
     0.04ns INFO     EXPECTED OUTPUT=0b1
     0.04ns INFO     DUT OUTPUT=0b10
     0.04ns INFO     EXPECTED OUTPUT=0b10
     0.04ns INFO     DUT OUTPUT=0b111
     0.04ns INFO     EXPECTED OUTPUT=0b100
     0.04ns INFO     DUT OUTPUT=0b100
     0.04ns INFO     EXPECTED OUTPUT=0b100
     0.04ns INFO     run_test2 failed
                     Traceback (most recent call last):
                       File "/workspace/challenges-vkhrishi/level3_design_buggy/test.py", line 122, in run_test2
                         assert dut_output_light_MT == expected_light_MT, error_message
                     AssertionError: Value mismatch DUT = 0b111 does not match MODEL = 0b100
``` 
Error 3 when No_of_vehical = 5
```
0.04ns INFO     running run_test3 (3/6)
     0.06ns INFO     DUT OUTPUT=0b1
     0.06ns INFO     EXPECTED OUTPUT=0b1
     0.06ns INFO     DUT OUTPUT=0b100
     0.06ns INFO     EXPECTED OUTPUT=0b100
     0.06ns INFO     DUT OUTPUT=0b1
     0.06ns INFO     EXPECTED OUTPUT=0b1
     0.06ns INFO     DUT OUTPUT=0b0
     0.06ns INFO     EXPECTED OUTPUT=0b100
     0.06ns INFO     run_test3 failed
                     Traceback (most recent call last):
                       File "/workspace/challenges-vkhrishi/level3_design_buggy/test.py", line 175, in run_test3
                         assert dut_output_light_S == expected_light_S, error_message
                     AssertionError: Value mismatch DUT = 0b0 does not match MODEL = 0b100
```

Error 4 when No_of_vehical = 4
```
 0.06ns INFO     running run_test4 (4/6)
     0.08ns INFO     DUT OUTPUT=0b0
     0.08ns INFO     EXPECTED OUTPUT=0b10
     0.08ns INFO     DUT OUTPUT=0b100
     0.08ns INFO     EXPECTED OUTPUT=0b100
     0.08ns INFO     DUT OUTPUT=0b10
     0.08ns INFO     EXPECTED OUTPUT=0b10
     0.08ns INFO     DUT OUTPUT=0b100
     0.08ns INFO     EXPECTED OUTPUT=0b100
     0.08ns INFO     run_test4 failed
                     Traceback (most recent call last):
                       File "/workspace/challenges-vkhrishi/level3_design_buggy/test.py", line 220, in run_test4
                         assert dut_output_light_M1 == expected_light_M1, error_message
                     AssertionError: Value mismatch DUT = 0b0 does not match MODEL = 0b10
```
 
Error 5 when No_of_vehical = 3
```
0.08ns INFO     running run_test5 (5/6)
     0.10ns INFO     DUT OUTPUT=0b100
     0.10ns INFO     EXPECTED OUTPUT=0b100
     0.10ns INFO     DUT OUTPUT=0b10
     0.10ns INFO     EXPECTED OUTPUT=0b100
     0.10ns INFO     DUT OUTPUT=0b100
     0.10ns INFO     EXPECTED OUTPUT=0b100
     0.10ns INFO     DUT OUTPUT=0b1
     0.10ns INFO     EXPECTED OUTPUT=0b1
     0.10ns INFO     run_test5 failed
                     Traceback (most recent call last):
                       File "/workspace/challenges-vkhrishi/level3_design_buggy/test.py", line 273, in run_test5
                         assert dut_output_light_M2 == expected_light_M2, error_message
                     AssertionError: Value mismatch DUT = 0b10 does not match MODEL = 0b100
```

Error 6 when No_of_vehical = 6
```
 0.10ns INFO     running run_test6 (6/6)
     0.12ns INFO     DUT OUTPUT=0b100
     0.12ns INFO     EXPECTED OUTPUT=0b100
     0.12ns INFO     DUT OUTPUT=0b100
     0.12ns INFO     EXPECTED OUTPUT=0b100
     0.12ns INFO     DUT OUTPUT=0b0
     0.12ns INFO     EXPECTED OUTPUT=0b100
     0.12ns INFO     DUT OUTPUT=0b10
     0.12ns INFO     EXPECTED OUTPUT=0b10
     0.13ns INFO     run_test6 failed
                     Traceback (most recent call last):
                       File "/workspace/challenges-vkhrishi/level3_design_buggy/test.py", line 326, in run_test6
                         assert dut_output_light_MT == expected_light_MT, error_message
                     AssertionError: Value mismatch DUT = 0b0 does not match MODEL = 0b100
```
## Test Scenario  (Important)

### 1
- Test Inputs: No_of_vehicle=7
- Expected Output:expected_light_M1 = 0b001,
    expected_light_M2 = 0b001,
    expected_light_MT = 0b100,
    expected_light_S = 0b100. 
- Observed Output in the DUT  DUT OUTPUT=0b1,
        DUT OUTPUT=0b101,
        DUT OUTPUT=0b100,
        DUT OUTPUT=0b100.
      

### 2
- Test Inputs: No_of_vehicle=2
- Expected Output:  expected_light_M1 = 0b001,
    expected_light_M2 = 0b010,
    expected_light_MT = 0b100,
    expected_light_S = 0b100.
- Observed Output in the DUT DUT OUTPUT=0b1,
         DUT OUTPUT=0b10,
         DUT OUTPUT=0b111,
         DUT OUTPUT=0b100.
         
          

### 3
- Test Inputs: No_of_vehicle=5
- Expected Output:   expected_light_M1 = 0b001,
    expected_light_M2 = 0b100,
    expected_light_MT = 0b001,
    expected_light_S = 0b100.
- Observed Output in the DUT DUT OUTPUT=0b1,
      DUT OUTPUT=0b100,
      DUT OUTPUT=0b1,
      DUT OUTPUT=0b0.
  

### 4
- Test Inputs: No_of_vehicle=4
- Expected Output:  expected_light_M1 = 0b010,
    expected_light_M2 = 0b100,
    expected_light_MT = 0b010,
    expected_light_S = 0b100. 
- Observed Output in the DUT  DUT OUTPUT=0b0,
   DUT OUTPUT=0b100,
   DUT OUTPUT=0b10,
   DUT OUTPUT=0b100.


### 5
- Test Inputs: No_of_vehicle=3
- Expected Output:     expected_light_M1 = 0b100,
    expected_light_M2 = 0b100,
    expected_light_MT = 0b100,
    expected_light_S = 0b001.
- Observed Output in the DUT  DUT OUTPUT=0b100,
     DUT OUTPUT=0b10,
     DUT OUTPUT=0b100,
     DUT OUTPUT=0b1.
   

### 6
- Test Inputs: No_of_vehicle=6
- Expected Output:    expected_light_M1 = 0b100,
    expected_light_M2 = 0b100,
    expected_light_MT = 0b100,
    expected_light_S = 0b010.
- Observed Output in the DUT OUTPUT=0b100,
    DUT OUTPUT=0b100,
    DUT OUTPUT=0b0,
    DUT OUTPUT=0b10.
    

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following
```
                    S1:
                    begin
                       light_M1<=3'b001;
                       light_M2<=3'b101; ===> Bug1
                       light_MT<=3'b100;
                       light_S<=3'b100;
                    end
                    S2:
                    begin 
                       light_M1<=3'b001;
                       light_M2<=3'b010;
                       light_MT<=3'b111; ===> Bug2
                       light_S<=3'b100;
                    end
                    S3:
                    begin
                       light_M1<=3'b001;
                       light_M2<=3'b100;
                       light_MT<=3'b001;
                       light_S<=3'b000; ===> Bug3
                    end
                    S4:
                    begin
                       light_M1<=3'b000; ===> Bug4
                       light_M2<=3'b100;
                       light_MT<=3'b010;
                       light_S<=3'b100;
                    end
                    S5:
                    begin
                       light_M1<=3'b100;
                       light_M2<=3'b010; ===> Bug5
                       light_MT<=3'b100;
                       light_S<=3'b001;
                    end
                    S6:
                    begin 
                       light_M1<=3'b100;
                       light_M2<=3'b100;
                       light_MT<=3'b000; ===>Bug6
                       light_S<=3'b010;
                    end



```
For the Traffic Light Controller design, the logic at S1 should be ```light_M2<=3'b001; ```instead of ```light_M2<=3'b101; ```as in the design code.
The logic at S2 should be ``` light_MT<=3'b100; ``` instead of ```light_MT<=3'b111; ``` as in the design code.
The logic at S3 should be ```    light_S<=3'b100; ``` instead of```light_S<=3'b000; ``` as in the design code.
The logic at S4 should be ```   light_M1<=3'b010;``` instead of``` light_M1<=3'b000; ``` as in the design code.
The logic at S5 should be ```light_M2<=3'b100; ``` instead of``` light_M2<=3'b010; ``` as in the design code.
The logic at S6 should be ``` light_MT<=3'b100; ``` instead of```light_MT<=3'b000; ``` as in the design code.

## Design Fix
Updating the design and re-running the test makes the test pass.

![9](https://user-images.githubusercontent.com/59868949/182024550-ad854f3a-a20d-4cde-be2f-dddf9fa0bdd2.png)

The updated design is checked in level3_design_original
