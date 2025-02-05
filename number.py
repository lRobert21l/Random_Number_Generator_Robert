import random

# Vers 1
# def genereaza_nre():
#     numere = []
#     for i in range(6):
#         numere.append(random.randint(1, 49))
#     return numere

# Vers 2
# def genereaza_nre():
#     return [ random.randint(1, 49) for _ in range((6))]

# Vers 3
# def genereaza_nre():
#     numere = []
#     while len(numere) < 6:
#         nr = random.randint(1, 6)
#         if nr not in numere:
#             numere.append(nr)
#     return numere

# Vers 4 Unica
def genereaza_nre():
    numere = []
    posibilitati = list(range(1, 50))
    for i in range(6):
        pozitie = random.randint(0, 48 - i)
        numar_extras = posibilitati.pop(pozitie)
        numere.append(numar_extras)
    return numere

## TODO: Modificati programul astfel incat sa generati 6 numere random.

if __name__ == "__main__":

    print(genereaza_nre())