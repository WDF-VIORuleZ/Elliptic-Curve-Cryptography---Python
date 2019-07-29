#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

    This module implements modular arithmetic on GF(2), used by  
    eea_arithmetics_moudle and diffie_hellman_module

"""

"""
    Modular addition in GF_2^mod
    Aufagbe 1.1
"""
def mod_add(a:int, b:int, mod:int):
    return int(((a % mod) + (b % mod)) % mod)


"""
    Modular subtraction in GF_2^mod
    Aufgabe 1.1
"""
def mod_sub(a:int, b:int, mod:int):
    if b < 0:
        return mod_add(a, abs(b), mod)
    else:
        return int( ((a % mod) - (b % mod)) % mod )


"""
    Modular multipliction in GF_2^mod
    Aufgabe 1.2
"""
def mod_mul(a:int, b:int, mod:int):
    # basic case checks
    if b == 1:
        return a
    elif a == 1:
        return b
    elif a == 0 or b == 0:
        return 0
    
    result = a

    for i in range(b):
        result = mod_add(result, b, mod)
        result %= mod

    return result


"""
    extended_euclidian_algorithm returns a tuple containing (r,s,t), whereas t is the inverse of element % mod
    The function takes two arguments: the elemnt itself and the moudle
    Aufgabe 1.4
"""
def extended_euclidian_algorithm_rec(a:int, b:int):
    if b == 0:
        return (a, 1, 0)
    
    (d_1, s_1, t_1) = extended_euclidian_algorithm_rec(b, a % b)
    (d, s, t) = (d_1, t_1, s_1 - (a // b)* t_1 )
    return (d, s, t)

"""
    This function must be used instead of th extended_euclidian_algorithm (recursive)
"""
def extended_euclidian_algorithm_wrapper(a:int, b:int):
    return (extended_euclidian_algorithm_rec(a,b)[1]) % b


"""
    Square-And-Multiply algorithm used for fast and efficient exponention of natural numbers in GF_2^mdo
"""
def sqaure_and_multiply(base:int, exp:int, mod:int):
    exp_bin = bin(exp)[3:]
    result = base

    for elem in exp_bin:
        result = (result**2) % mod

        if elem == '1':
            result = (result * base) % mod

    return result


"""
    Fermat's little theorem calculates the modular inverse of a in GF_2^p
    This function makes us of the frequently introduced function sqaure_and_multiply
    Aufgabe 1.3
"""
def fermats_little_theorem(a:int, p:int):
    return sqaure_and_multiply(a, p-2, p)
    


