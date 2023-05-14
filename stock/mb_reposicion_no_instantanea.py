import mb
from math import sqrt

def t1(q, p): return q / p

def S(q, d, p): return q * (1 - d/p)

"""
Costo total esperado de un ciclo i
"""
def CTEi(b, D, k, t, C1, q, p): return b*q + 0.5 * S(q, D, p) * C1*t + k

"""
Costo total esperado de todo el periodo
"""
def CTE(b, D, k, T, C1, q, p): return (D / q) * CTEi(b, D, k, T*q/D, C1, q, p)

"""
Tamaño del lote optimo de compra

def qo(k, D, T, C1, P): return sqrt((2*k*D)/(T*C1*(1 - D/P)))
"""
def qo(k, D, T, C1, P): return mb.qo(k, D, T, C1) / sqrt(1 - D/P)

"""
Costo total esperado optimo

def CTEo(b, D, k, T, C1, P): return CTE(b, D, k, T, C1, qo(k, D, T, C1, P), P)
"""
def CTEo(b, D, k, T, C1, P): return b*D + sqrt(2*k*D*T*C1*(1 - D/P))

