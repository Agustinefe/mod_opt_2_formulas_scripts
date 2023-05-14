from math import sqrt

"""
Tamaño del lote optimo de compra
"""
def qo(k, D, T, C1): return sqrt((2*k*D)/(T*C1))

"""
Costo total esperado de un ciclo i
"""
def CTEi(b, k, t, C1, q): return b*q + 0.5*q*C1*t + k

"""
Costo total esperado de todo el periodo
"""
def CTE(b, D, k, T, C1, q): return (D / q) * CTEi(b, k, T*q/D, C1, q)

"""
Costo total esperado optimo

def CTEo(b, D, k, T, C1): return CTE(b, D, k, T, C1, qo(k, D, T, C1))
"""
def CTEo(b, D, k, T, C1): return b*D + sqrt(2*k*D*T*C1)

"""
Intervalo optimo de cada ciclo
"""
def to(k, D, T, C1): return qo(k, D, T, C1) * (T / D)

"""
Nro optimo de pedidos a efectuar
"""
def no(k, D, T, C1): return D / qo(k, D, T, C1)

"""
Stock de reorden
"""
def SR(LT, D): return LT*D