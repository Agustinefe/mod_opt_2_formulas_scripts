import mb
from math import sqrt

"""
Tamaño del lote optimo de compra
"""
def qo(k, D, T, C1, C2): return mb.qo(k, D, T, C1) * sqrt((C1 + C2) / C2)

"""
Stock maximo optimo
"""
def So(k, D, T, C1, C2): return mb.qo(k, D, T, C1) * sqrt(C2 / (C1 + C2))

"""
Costo total esperado optimo
"""
def CTEo(b, D, k, T, C1, C2): return b*D + sqrt(2*k*D*T*C1) * sqrt(C2 / (C1 + C2))

"""
Cantidad maxima optima de cantidades agotadas
"""
def SAo(k, D, T, C1, C2): return qo(k, D, T, C1, C2) - So(k, D, T, C1, C2)

"""
Intervalo optimo de cada ciclo
"""
def to(k, D, T, C1, C2): return qo(k, D, T, C1, C2) * (T / D)

"""
Periodo optimo de entrega

def t1o(k, D, T, C1, C2): return So(k, D, T, C1, C2) * (to(k, D, T, C1, C2) / qo(k, D, T, C1, C2))
"""
def t1o(k, D, T, C1, C2): return So(k, D, T, C1, C2) * (T / D)

"""
Periodo optimo de deficit

def t2o(k, D, T, C1, C2): return (qo(k, D, T, C1, C2) - So(k, D, T, C1, C2)) * (to(k, D, T, C1, C2) / qo(k, D, T, C1, C2))
"""
def t2o(k, D, T, C1, C2): return to(k, D, T, C1, C2) - t1o(k, D, T, C1, C2)

"""
Nro optimo de pedidos a efectuar
"""
def no(k, D, T, C1, C2): return D / qo(k, D, T, C1, C2)

"""
Stock de reorden
"""
def SR(LT, D, k, T, C1, C2): return mb.SR(LT, D) - SAo(k, D, T, C1, C2)