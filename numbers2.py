import random

# Vers 1
# def genereaza_nre():
#     numere = []
#     for i in range(6):
#         numere.append(random.randint(1, 49))
#     return numere

# Vers 2
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