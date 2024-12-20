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
print(register)
print(program)

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
    old_pointer  = pointer
    old_register = register.copy()
    pointer += 2
    register['A'] = register['A'] // 2 ** get_combo(operand, register)
    print('adv', operand, old_pointer, pointer, old_register, register)
    return pointer, register

def instruction_bxl(operand, pointer, register):
    old_pointer  = pointer
    old_register = register.copy()
    pointer += 2
    register['B'] = register['B'] ^ get_literal(operand)
    print('bxl', operand, old_pointer, pointer, old_register, register)
    return pointer, register

def instruction_bst(operand, pointer, register):
    old_pointer  = pointer
    old_register = register.copy()
    pointer += 2
    register['B'] = get_combo(operand, register) % 8
    print('bst', operand, old_pointer, pointer, old_register, register)
    return pointer, register

def instruction_jnz(operand, pointer, register):
    old_pointer  = pointer
    old_register = register.copy()
    if register['A'] != 0:
        pointer = get_literal(operand)
    else:
        pointer += 2
    print('jnz', operand, old_pointer, pointer, old_register, register)
    return pointer, register

def instruction_bxc(operand, pointer, register):
    old_pointer  = pointer
    old_register = register.copy()
    pointer += 2
    register['B'] = register['B'] ^ register['C']
    print('bxc', operand, old_pointer, pointer, old_register, register)
    return pointer, register

def instruction_out(operand, pointer, register):
    old_pointer  = pointer
    old_register = register.copy()
    pointer += 2
    output.append(get_combo(operand, register) % 8)
    print('out', operand, old_pointer, pointer, old_register, register)
    return pointer, register

def instruction_bdv(operand, pointer, register):
    old_pointer  = pointer
    old_register = register.copy()
    pointer += 2
    register['B'] = register['A'] // 2 ** get_combo(operand, register)
    print('bdv', operand, old_pointer, pointer, old_register, register)
    return pointer, register

def instruction_cdv(operand, pointer, register):
    old_pointer  = pointer
    old_register = register.copy()
    pointer += 2
    register['C'] = register['A'] // 2 ** get_combo(operand, register)
    print('cdv', operand, old_pointer, pointer, old_register, register)
    return pointer, register

instruction = [
    instruction_adv,
    instruction_bxl,
    instruction_bst,
    instruction_jnz,
    instruction_bxc,
    instruction_out,
    instruction_bdv,
    instruction_cdv,
]

pointer = 0
output = []
while pointer < len(program):
    opcode = program[pointer]
    operand = program[pointer+1]
    print(opcode, operand)
    pointer, register = instruction[opcode](operand, pointer, register)

t1 = time.perf_counter()
print(f"Answer: {output}")
print(f"Answer: {','.join(str(_) for _ in output)}")
print(f"Execution time: {t1 - t0:.6f} seconds")
