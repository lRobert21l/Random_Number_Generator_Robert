from bilet import joaca_bilet
from numbers2 import genereaza_nre

jucate = joaca_bilet()
castigatoare = genereaza_nre()

print("Ai jucat:", jucate)
print("Au fost extrase:", castigatoare)

nimerite = [ nr for nr in jucate if nr in castigatoare]
print("Ai numerit:", nimerite)

# Categoria 1 - trebuie sa fie ghicite 6
# Categoria 2 - trebuie sa fie ghicite 5
# Categoria 3 - trebuie sa fie ghicite 4
# Categoria 4 - trebuie sa fie ghicite 3

categorii = {
    6:1,
    5:2,
    4:3,
    3:4
}

print("Categoria", categorii.get(len(nimerite), "lipsa"))