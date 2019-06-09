# Example LLVM/antlr4 Language

- Written mostly in python
- Lexer and parser written using antlr4
- Machine code generated using LLVM
- Currently only constant integer expression evaluation works

## Requirements
- LLVM 8
- antlr4
- Python3
- pip3

## Setup

```bash
sudo apt-get install llvm
sudo apt-get install antlr4
sudo pip3 install -r requirements.txt
```

## Running
```bash
./run.sh
```
This will run the compiler and emit an object file, then link it to the bootstrap main.c using gcc and run the executable.
Edit ./test/example.code to test another expressions.

## Inspecting
```bash
objdump -d ./out/evaluate.o
```

## Example language syntax

```c

int fibbonacci(int n) {
   if(n == 0){
      return 0
   }
   
   if(n == 1) {
      return 1
   }

    return fibbonacci(n-1) + fibbonacci(n-2)
}

int start() {
    return fibbonacci(10)
}
```

## Features
- Function definitions
- Assignment statement
- int, double types
- Expression evaluation
- Function calls
- Auto cast to double
- Return statement
