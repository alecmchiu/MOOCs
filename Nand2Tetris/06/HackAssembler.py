#!/usr/bin/env python3

import sys

c_instruction_table = {
	'0' : '101010',
	'1' : '111111',
	'-1' : '111010',
	'D' : '001100',
	'A' : '110000',
	'M' : '110000',
	'!D' : '001101',
	'!A' : '110001',
	'!M' : '110001',
	'-D' : '001111',
	'-A' : '110011',
	'-M' : '110011',
	'D+1' : '011111',
	'A+1' : '110111',
	'M+1' : '110111',
	'D-1' : '001110',
	'A-1' : '110010',
	'M-1' : '110010',
	'D+A' : '000010',
	'D-A' : '010011',
	'A-D' : '000111',
	'D&A' : '000000',
	'D|A' : '010101',
	'D+M' : '000010',
	'D-M' : '010011',
	'M-D' : '000111',
	'D&M' : '000000',
	'D|M' : '010101'
}

destination_jump_table = {
	'M' : '001',
	'D' : '010',
	'MD' : '011',
	'A' : '100',
	'AM' : '101',
	'AD' : '110',
	'AMD' : '111',
	'JGT' : '001',
	'JEQ' : '010',
	'JGE' : '011',
	'JLT' : '100',
	'JNE' : '101',
	'JLE' : '110',
	'JMP' : '111'
}

def parse(line):
	output_string = '111'
	if ';' in line:
		jump = line.split(';')[-1]
		jump_code = destination_jump_table[jump]
	else:
		jump_code = '000'	
	computation = line.split(';')[0]
	if '=' in line:
		computation = computation.split('=')
		if 'M' in computation[1]:
			output_string = output_string + '1'
		else:
			output_string = output_string + '0'
		output_string = output_string + c_instruction_table[computation[1]]
		output_string = output_string + destination_jump_table[computation[0]]
	else:
		if 'M' in computation[0]:
			output_string = output_string + '1'
		else:
			output_string = output_string + '0'
		output_string = output_string + c_instruction_table[computation[0]]
		output_string = output_string + '000'
	output_string = output_string + jump_code + '\n'
	return output_string

def create_symbol_table(input_file):
	symbols = {
		'SP' : 0, 
		'LCL' : 1, 
		'ARG' : 2, 
		'THIS' : 3, 
		'THAT' : 4, 
		'SCREEN' : 16384, 
		'KBD' : 24576
	}
	for i in range(16):
		reg = 'R' + str(i)
		symbols[reg] = i
	command_number = 0
	for line in input_file:
		stripped_line = line.strip().rstrip()
		if stripped_line == '':
			continue
		elif stripped_line[0] == '/':
			continue
		elif stripped_line[0] == '(':
				symbols[stripped_line[1:len(stripped_line)-1]] = command_number
		else:
			command_number += 1
	input_file.seek(0)
	return symbols

if __name__ == '__main__':
	if (len(sys.argv) != 2):
		print("Usage: python HackAssembler.py input_file.asm",file=sys.stderr)
		exit(1)
	source_file = open(sys.argv[1], 'r')
	output_filename = sys.argv[1][:len(sys.argv[1])-3] + "hack"
	output_file = open(output_filename, 'w')
	table = create_symbol_table(source_file)
	open_register = 16
	for line in source_file:
		stripped_line = line.strip().rstrip()
		if stripped_line == '':
			continue
		if stripped_line[0] == '/' or stripped_line[0] == '(':
			continue
		comment_index = stripped_line.find('/')
		if comment_index != -1:
			stripped_line = stripped_line[:comment_index]
			stripped_line = stripped_line.strip().rstrip()
		if stripped_line[0] == '@':
			address = stripped_line[1:]
			if address.isdigit():
				binary_address = bin(int(address))[2:].zfill(16) +'\n'
			elif address not in table:
				table[address] = open_register
				open_register += 1
				binary_address = bin(table[address])[2:].zfill(16) + '\n'
			else:
				binary_address = bin(table[address])[2:].zfill(16) + '\n'
			output_file.write(binary_address)
		else:
			output_file.write(parse(stripped_line))
	source_file.close()
	output_file.close()
	exit(0)

