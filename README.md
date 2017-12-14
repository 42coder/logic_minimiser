# Optimised Implementation of Logic Functions

This is a python based program that can be used to minimize multi-bit input expressions. The code does this by first expanding each multiplication and addition and then reducing the expression for each of the bits generated. 

## Getting Started

The code is written in python and does not require any external dependencies other than a Python interpreter.

A link to our project report can be found [here](https://drive.google.com/open?id=19p2KjeI9Yep3EquI8GEGlSfuSY2_oTeh).

### Using the Optimizer

To run the optimizer you will need to run the file *ds_mainInput.py*.

Then for giving the inputs we do
```
Enter the variable names:	abc
Enter the size of a		2
Enter the size of b		3
Enter the size of c		1
Enter the Boolean Expression:	abc+a
```
Where a, b and c are the variable names that we are going to use. 

### Working of the Optimizer

Since ‘a’ is of size 2 in the above example, it is treated as a sequence of bits named a0 and a1. In the code, the index 0 is treated as the LSB. 

The optimizer, to show its working, prints the expression generated when it expands the expression bitwise and its respective cubes, the minimised expression of each bit and the corresponding verilog files generated. It also generates .txt files for each verilog file to be generated.

### Fixes and Improvements

* A heuristic algorithm (like the [Espresso logic minimizer](https://en.wikipedia.org/wiki/Espresso_heuristic_logic_minimizer)) could be used to speed up the program.

