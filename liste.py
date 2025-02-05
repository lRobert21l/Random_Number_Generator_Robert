numere = []

posibilitati = list(range(1, 50))
print(posibilitati)

posibilitati.remove(10)
print(posibilitati)
numere.append(10)

# 0... 47
print(posibilitati[47])

posibilitati.remove(22)
numere.append(22)
print(posibilitati)
print(posibilitati[46])

posibilitati = list(range(1, 50))
posibilitati.pop(30)
print(posibilitati)