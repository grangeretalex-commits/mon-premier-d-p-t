# Programme financier TI-84 Plus CE-T
# Interets, actualisation, annuites
# Optimise memoire TI-84

# Periodicites: nb de periodes/an
# 1:quinzaine(24) 2:mois(12) 3:trim(4)
# 4:semestre(2) 5:annuel(1)
_P = (24, 12, 4, 2, 1)

def sper():
    print("Periodicite taux:")
    print("1:Quinzaine 2:Mois")
    print("3:Trim 4:Sem 5:An")
    return int(input("Choix: "))

def taux_an():
    t = float(input("Taux(%): ")) / 100
    p = sper()
    # Conversion en taux annuel equiv.
    f = _P[p - 1]
    if f == 1:
        return t
    return (1 + t) ** f - 1

def menu():
    print("=== FINANCE ===")
    print("1:Interet simple")
    print("2:Interet compose")
    print("3:Actualisation")
    print("4:Annuite remb.")
    print("5:Tableau amort.")
    print("0:Quitter")
    return int(input("Choix: "))

def interet_simple():
    c = float(input("Capital: "))
    t = taux_an()
    n = float(input("Duree(ans): "))
    i = c * t * n
    print("Taux annuel:", round(t * 100, 4), "%")
    print("Interet:", round(i, 2))
    print("Montant:", round(c + i, 2))

def interet_compose():
    c = float(input("Capital: "))
    t = taux_an()
    n = int(input("Nb annees: "))
    p = int(input("Comp/an(1,2,4,12,24): "))
    m = c * (1 + t / p) ** (n * p)
    print("Taux annuel:", round(t * 100, 4), "%")
    print("Montant:", round(m, 2))
    print("Interets:", round(m - c, 2))

def actualisation():
    vf = float(input("Valeur future: "))
    t = taux_an()
    n = int(input("Nb annees: "))
    va = vf / (1 + t) ** n
    print("Taux annuel:", round(t * 100, 4), "%")
    print("Val actuelle:", round(va, 2))

def annuite_remb():
    c = float(input("Capital: "))
    t = taux_an()
    n = int(input("Nb mensualites: "))
    tm = (1 + t) ** (1 / 12) - 1
    if tm == 0:
        a = c / n
    else:
        a = c * tm / (1 - (1 + tm) ** (-n))
    print("Taux annuel:", round(t * 100, 4), "%")
    print("Mensualite:", round(a, 2))
    print("Cout total:", round(a * n, 2))
    print("Cout interet:", round(a * n - c, 2))

def tableau_amort():
    c = float(input("Capital: "))
    t = taux_an()
    n = int(input("Nb mensualites: "))
    tm = (1 + t) ** (1 / 12) - 1
    if tm == 0:
        a = c / n
    else:
        a = c * tm / (1 - (1 + tm) ** (-n))
    r = c
    print("Taux annuel:", round(t * 100, 4), "%")
    print("M|Mens|Inter|Cap|Reste")
    for k in range(1, n + 1):
        it = r * tm
        cp = a - it
        r = r - cp
        if r < 0:
            r = 0
        print(k, round(a, 1), round(it, 1),
              round(cp, 1), round(r, 1))
        if k % 12 == 0 and k < n:
            input("[Suite...]")

# Boucle principale
while True:
    c = menu()
    if c == 1:
        interet_simple()
    elif c == 2:
        interet_compose()
    elif c == 3:
        actualisation()
    elif c == 4:
        annuite_remb()
    elif c == 5:
        tableau_amort()
    elif c == 0:
        break
    input("[OK]")
