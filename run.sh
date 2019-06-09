#!/usr/bin/env bash

# Clean previous builds
rm -rf out
mkdir out

# Compile start
as ./bootstrap/start.s -o ./out/start.o

# Compile stdlib
clang -shared -nostdlib -O3 ./bootstrap/stdlib.c -o ./out/stdlib.o

# Compile the program
python3 ./run.py

# Link everything
ld -dynamic-linker /lib64/ld-linux-x86-64.so.2 -o ./out/program ./out/program.o ./out/start.o ./out/stdlib.o

# Dump executable
objdump -d ./out/program

# Run executable
./out/program