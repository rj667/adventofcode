#!/usr/bin/env python3

import sys
import time
from pprint import pprint
import re

t0 = time.perf_counter()

infile = sys.argv[1:] and sys.argv[1] or "input.txt"

total = 0
register = []; A=0; B=1; C=2
program = []
with open(infile, 'r') as file:
    for line in file:
        if (match := re.match(r'Register (\w): (\d+)', line)):
            register.append(int(match.group(2)))
        if (match := re.match(r'Program: (.*)', line)):
            program = [int(char) for char in match.group(1).replace(',','')]
print(f'program: {program}')
print(f'register:   {register}')

def get_literal(operand):
    return operand

def get_combo(operand, register):
    if operand < 4:
        return operand
    else:
        return register[operand-4]

def set_register_by_combo(operand, register, value):
    if operand < 4:
        noop
    else:
        register[operand-4] = value

def do_adv(operand, pointer, register):
    register[A] = register[A] // 2 ** get_combo(operand, register)
    return pointer+2, register

def do_inv_adv(operand, pointer, register):
    register[A] = register[A] * 2 ** get_literal(operand)
    return pointer-2, register

def do_bxl(operand, pointer, register):
    register[B] = register[B] ^ get_literal(operand)
    return pointer+2, register

def do_inv_bxl(operand, pointer, register):
    return pointer-2, register

def do_bst(operand, pointer, register):
    register[B] = get_combo(operand, register) % 8
    return pointer+2, register

def do_inv_bst(operand, pointer, register):
    return pointer-2, register

def do_jnz(operand, pointer, register):
    if register[A] != 0:
        pointer = get_literal(operand)
    else:
        pointer += 2
    return pointer, register

def do_inv_jnz(operand, pointer, register):
    return pointer-2, register

def do_bxc(operand, pointer, register):
    register[B] = register[B] ^ register[C]
    return pointer+2, register

def do_inv_bxc(operand, pointer, register):
    return pointer-2, register

def do_out(operand, pointer, register):
    output.append(get_combo(operand, register) % 8)
    return pointer+2, register

def do_inv_out(operand, pointer, register):
    remainder = output.pop(0)
    value = get_combo(operand, register)
    new_value = value - value % 8 + remainder - 8
    set_register_by_combo(operand, register, new_value)
    return pointer-2, register

def do_bdv(operand, pointer, register):
    register[B] = register[A] // 2 ** get_combo(operand, register)
    return pointer+2, register

def do_inv_bdv(operand, pointer, register):
    return pointer-2, register

def do_cdv(operand, pointer, register):
    register[C] = register[A] // 2 ** get_combo(operand, register)
    return pointer+2, register

def do_inv_cdv(operand, pointer, register):
    return pointer-2, register

instruction = [
    do_inv_adv,    #0
    do_inv_bxl,    #1
    do_inv_bst,    #2
    do_inv_jnz,    #3
    do_inv_bxc,    #4
    do_inv_out,    #5
    do_inv_bdv,    #6
    do_inv_cdv,    #7
]

pointer = len(program)-2
output = program.copy()
while pointer >= 0:
    opcode = program[pointer]
    operand = program[pointer+1]
    print(f'{pointer:3} {str(register):45} {opcode} {instruction[opcode].__name__[-7:]} {operand}', end=' ')
    pointer, register = instruction[opcode](operand, pointer, register)
    print(f'{pointer:4} {str(register):45s} {output}')

output = ','.join(str(_) for _ in output)
t1 = time.perf_counter()
print(f"Output: {output}")
print(f"Execution time: {t1 - t0:.6f} seconds")
