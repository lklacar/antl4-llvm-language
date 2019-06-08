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

int add(int b, int c, int d) {
    return b+c+d
}

int start() {
    int c = add(1,2,3)
    return c
}
```