# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 18:24:24 2024

@author: jumaf
"""

def cuadrado(n):
    return n*n

def test_cuadrado():
    print('Voy a probar la función cuadrado...')
    assert(cuadrado(2)==4)
    assert(cuadrado(3)==6)
    
    print('pasó los tests...')

test_cuadrado()
