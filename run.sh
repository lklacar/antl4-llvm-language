#!/usr/bin/env bash

rm -rf out
mkdir out

printf "Compiling...\n"
python3 compiler.py

printf "Linking...\n"
gcc ./bootstrap/main.c ./out/evaluate.o -o ./out/main

printf "Object dump...\n"
objdump -d ./out/evaluate.o

printf "Running...\n"
./out/main