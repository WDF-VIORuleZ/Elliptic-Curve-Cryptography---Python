#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from dataclasses import dataclass
from gf2_arithmetics_module import fermats_little_theorem, extended_euclidian_algorithm_wrapper

"""

    In the project two new class are implemented, ecc_curve and ecc_point
    ecc_curve's main purpose is storing the curves paramaters a, b and p
    ecc_point serves as a representation of ellipitic curve points, operators are overloaded ( overloaded addition uses fermat for inversion )

"""
@dataclass
class ecc_curve:
    a: int
    b: int
    p: int

    def __init__(self, m_a, m_b, m_p):
        self.a = m_a
        self.b = m_b
        self.p = m_p


@dataclass
class ecc_point:
    x: int
    y: int

    def __init__(self, m_x:int, m_y:int):
        self.x = m_x
        self.y = m_y

    def __add__(self, other):
        result = add_points(self, other)
        self.x = result.x
        self.y = result.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Overloaded inversion operator for naf_point_mul
    def __inv__(self):
        self.y *= (-1)
        


"""
    The following functions can be called using fermat (default type) or using eea (extended euclidian algorithm) both implemented in gf2_arithmetics_module
    
    Change 'mode' value in function call, i.e. add_points(P, Q, E,'eea')
    Function returns a point as the sum of P and Q or doubles the point P
    Calling the functions with invalid arguments results in None return Tpye

    Aufgaben 2.1, 2.2

"""


def double_point(P:ecc_point, E:ecc_curve, mode:str='fermat'):
    if mode == 'fermat' or mode == 'eea':    
        s = 0

        if mode == 'fermat':
            s = fermats_little_theorem(2 * P.y, E.p) * (3 * pow(P.x,2) + E.a) % E.p

        else:
            s = extended_euclidian_algorithm_wrapper(2 * P.y, E.p) * (3 * pow(P.x, 2) + E.a) %  E.p

        x3 = (pow(s,2) - P.x - P.x) % E.p
        y3 = (s * (P.x - x3) - P.y) % E.p

        return ecc_point(x3, y3)

    else:
        return None


def add_points(P:ecc_point, Q:ecc_point, E:ecc_curve, mode:str='fermat'):
    if mode == 'fermat' or mode == 'eea':    
        s = 0

        if mode == 'fermat':
            s = (( Q.y - P.y ) % E.p) * fermats_little_theorem((Q.x - P.x) % E.p, E.p) % E.p

        else:
            s = (( Q.y - P.y ) % E.p) * extended_euclidian_algorithm_wrapper(Q.x - P.x, E.p) % E.p    

        x3 = (pow(s,2) - P.x - Q.x) % E.p
        y3 = (s * (P.x - x3) - P.y) % E.p

        return ecc_point(x3, y3)

    else:
        return None


"""

    Point multiplication using Double-and-Add Algorithm
    P: ecc_point, k: skalar factor from Z_p*
    Aufgabe 2.3

"""
def mul_point(k:int, P:ecc_point, E:ecc_curve, mode:str='fermat'):
    
    bin_exp     = bin(k)[3:]
    bin_exp_rev = bin(k)[3:][::-1]

    #print("bin_exps: " + bin_exp + " " + bin_exp_rev)

    T = P

    for elem in bin_exp:
        #print(f"[init] T ({T.x},{T.y})")
        T = double_point(T,E, mode)
        #print(f"[DOUBLE] T: ({T.x},{T.y})")

        if elem == '1':
            T = add_points(T, P, E, mode)
            #print(f"\t[ADD] T: ({T.x},{T.y})")

    return T

"""
    
"""
def non_adjecent_form_expo(e:int):
    X = e
    res = []
    
    while X >= 1:
        if X % 2 != 0:
            res.insert(0, 2 - (X % 4))
            X -= res[0]
        else:
            res.insert(0, 0)
        
        X //= 2

    return res


"""
    Point multiplication using the 'non adjecent form'
    Aufgabe 2.4
"""
def naf_point_mul(naf_exp:list, P:ecc_point, E:ecc_curve, mode:str="fermat"):
    Q = ecc_point(0, 0)

    for elem in naf_exp[::-1]:
        Q = mul_point(2, Q, E, mode)

        if elem == "1":
            Q = add_points(Q, P, E, mode)
        if  elem == "-1":
            Q = add_points(Q, ~P, E, mode)

    return Q


