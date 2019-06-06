#!/usr/bin/env bash

rm -rf out
mkdir out
python3 compiler.py

gcc ./c/main.c ./out/evaluate.o -o ./out/main

./out/main