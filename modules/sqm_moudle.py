#! /bin/python3

def to_bit_list(x):
    if x == 0: return [0]
    bit = []
    while x:
        bit.append(x % 2)
        x >>= 1
    return bit[::-1]


def sqml(base:str, exponent:int, bin_expo:str, modulo:int):
	result = base

	for var in bin_expo:
		if bool(var):
			result = (result * base) % modulo
		else:
			result = (result * result) % modulo

	return result