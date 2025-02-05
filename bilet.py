from number import genereaza_nre

# call function > genereaza_nre (a, b)

def joaca_bilet():
    bilet = []
    while len(bilet) < 6:

        nr = (input("Introduceti un numar:\n"))
        try:
            nr = int(nr)
        except:
            print("Nu este un numar..")
            continue

        if nr not in range(1, 50):
            print("Numerele trebuie sa fie de la 1 la 49")
            continue
        elif nr in bilet:
            print("Numarul a fost deja jucat")

        else:
            bilet.append(nr)
            if len(bilet) < 6:
                print("Mai aveti de introdus",6-len(bilet),"numere")

    return bilet

if __name__ == "__main__":
    joaca_bilet()