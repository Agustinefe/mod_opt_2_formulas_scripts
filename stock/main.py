import mb
import mb_stock_proteccion as mbsp
import mb_agotamiento as mba
import mb_reposicion_no_instantanea as mbrni
import mb_descarga_instantanea as mbdi

import json

with open("params.json", "r") as f:
    p = json.load(f)


print(mb.SR(p["LT"], p["D"]))