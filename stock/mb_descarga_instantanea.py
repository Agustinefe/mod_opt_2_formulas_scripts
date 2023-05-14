import mb

"""
Costo total esperado de un ciclo i
"""
def CTEi(b, k, t, C1, q): return mb.CTEi(b, k, t, C1, q)

"""
Costo total esperado de todo el periodo
"""
def CTE(b, P, k, T, C1, q): return mb.CTE(b, P, k, T, C1, q)

"""
Tamaño del lote optimo de descarga
"""
def qo(k, P, T, C1): return mb.qo(k, P, T, C1)

"""
Costo total esperado optimo

def CTEo(b, P, k, T, C1): return CTE(b, P, k, T, C1, qo(k, P, T, C1))
"""
def CTEo(b, P, k, T, C1): return mb.CTEo(b, P, k, T, C1)

"""
Intervalo optimo de cada ciclo
"""
def to(k, P, T, C1): return mb.to(k, P, T, C1)

"""
Nro optimo de pedidos a efectuar
"""
def no(k, P, T, C1): return mb.no(k, P, T, C1)

"""
Stock de reorden
"""
def SR(LT, k, P, T, C1): return qo(k, P, T, C1) - LT*P