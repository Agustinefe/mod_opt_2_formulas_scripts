import mb

"""
Tamaño del lote optimo de compra
"""
def qo(k, D, T, C1): return mb.qo(k, D, T, C1)

"""
Costo total esperado de todo el periodo
"""
def CTE(b, D, k, T, C1, q, SP): return mb.CTE(b, D, k, T, C1, q) + SP*C1*T

"""
Costo total esperado optimo
"""
def CTEo(b, D, k, T, C1, SP): return mb.CTEo(b, D, k, T, C1) + SP*C1*T

"""
Intervalo optimo de cada ciclo
"""
def to(k, D, T, C1): return mb.to(k, D, T, C1)

"""
Nro optimo de pedidos a efectuar
"""
def no(k, D, T, C1): return mb.no(k, D, T, C1)

"""
Stock de reorden
"""
def SR(LT, D, SP): return mb.SR(LT, D) + SP