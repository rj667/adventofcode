#!/usr/bin/env python3

import sys
import time
from pprint import pprint
import re

t0 = time.perf_counter()

infile = sys.argv[1:] and sys.argv[1] or "input.txt"

total = 0
register = {}
program = []
with open(infile, 'r') as file:
    for line in file:
        if (match := re.match(r'Register (\w): (\d+)', line)):
            register[match.group(1)] = int(match.group(2))
        if (match := re.match(r'Program: (.*)', line)):
            program = [int(char) for char in match.group(1).replace(',','')]
print(f'program: {program}')
print(f'register:   {register}')

def get_literal(operand):
    return operand

def get_combo(operand, register):
    match operand:
        case 0|1|2|3:
            return operand
        case 4:
            return register['A']
        case 5:
            return register['B']
        case 6:
            return register['C']
        case 7:
            sys.exit(f'illegal combo operand: {operand}')
    return operand

def instruction_adv(operand, pointer, register):
    register['A'] = register['A'] // 2 ** get_combo(operand, register)
    return pointer+2, register

def instruction_bxl(operand, pointer, register):
    register['B'] = register['B'] ^ get_literal(operand)
    return pointer+2, register

def instruction_bst(operand, pointer, register):
    register['B'] = get_combo(operand, register) % 8
    return pointer+2, register

def instruction_jnz(operand, pointer, register):
    if register['A'] != 0:
        pointer = get_literal(operand)
    else:
        pointer += 2
    return pointer, register

def instruction_bxc(operand, pointer, register):
    register['B'] = register['B'] ^ register['C']
    return pointer+2, register

def instruction_out(operand, pointer, register):
    output.append(get_combo(operand, register) % 8)
    return pointer+2, register

def instruction_bdv(operand, pointer, register):
    register['B'] = register['A'] // 2 ** get_combo(operand, register)
    return pointer+2, register

def instruction_cdv(operand, pointer, register):
    register['C'] = register['A'] // 2 ** get_combo(operand, register)
    return pointer+2, register

instruction = [
    instruction_adv,    #0
    instruction_bxl,    #1
    instruction_bst,    #2
    instruction_jnz,    #3
    instruction_bxc,    #4
    instruction_out,    #5
    instruction_bdv,    #6
    instruction_cdv,    #7
]

pointer = 0
output = []
while pointer < len(program):
    opcode = program[pointer]
    operand = program[pointer+1]
    print(f'{opcode} {instruction[opcode].__name__[-3:]} {operand} {pointer:3} {str(register):45}', end=' ')
    pointer, register = instruction[opcode](operand, pointer, register)
    print(f'{pointer:2} {str(register):45s} {output}')

output = ','.join(str(_) for _ in output)
t1 = time.perf_counter()
print(f"Output: {output}")
print(f"Execution time: {t1 - t0:.6f} seconds")
