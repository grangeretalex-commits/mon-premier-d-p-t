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

_N = ("Quinz.","Mois","Trim.","Sem.","An")

def svers():
    print("Periodicite versement:")
    print("1:Quinzaine 2:Mois")
    print("3:Trim 4:Sem 5:An")
    p = int(input("Choix: "))
    return p

def taux_per(t, p):
    f = _P[p - 1]
    return (1 + t) ** (1 / f) - 1

def menu():
    print("=== FINANCE ===")
    print("1:Interet simple")
    print("2:Interet compose")
    print("3:Actualisation")
    print("4:Annuite remb.")
    print("5:Tableau amort.")
    print("6:Annuite capital.")
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
    p = svers()
    tp = taux_per(t, p)
    n = int(input("Nb echeances: "))
    if tp == 0:
        a = c / n
    else:
        a = c * tp / (1 - (1 + tp) ** (-n))
    print("Taux annuel:", round(t * 100, 4), "%")
    print("Taux", _N[p-1], round(tp * 100, 4), "%")
    print("Echeance:", round(a, 2))
    print("Cout total:", round(a * n, 2))
    print("Cout interet:", round(a * n - c, 2))

def tableau_amort():
    c = float(input("Capital: "))
    t = taux_an()
    p = svers()
    tp = taux_per(t, p)
    n = int(input("Nb echeances: "))
    f = _P[p - 1]
    if tp == 0:
        a = c / n
    else:
        a = c * tp / (1 - (1 + tp) ** (-n))
    r = c
    print("Taux annuel:", round(t * 100, 4), "%")
    print("Taux", _N[p-1], round(tp * 100, 4), "%")
    print("N|Ech|Inter|Cap|Reste")
    for k in range(1, n + 1):
        it = r * tp
        cp = a - it
        r = r - cp
        if r < 0:
            r = 0
        print(k, round(a, 1), round(it, 1),
              round(cp, 1), round(r, 1))
        if k % f == 0 and k < n:
            input("[Suite...]")

def annuite_capit():
    print("1:Calcul versement")
    print("2:Calcul capital")
    ch = int(input("Choix: "))
    t = taux_an()
    p = svers()
    tp = taux_per(t, p)
    if ch == 1:
        vf = float(input("Capital vise: "))
        n = int(input("Nb echeances: "))
        if tp == 0:
            a = vf / n
        else:
            a = vf * tp / ((1 + tp) ** n - 1)
        print("Taux annuel:", round(t * 100, 4), "%")
        print("Taux", _N[p-1], round(tp * 100, 4), "%")
        print("Versement:", round(a, 2))
        print("Total verse:", round(a * n, 2))
        print("Interets gagnes:",
              round(vf - a * n, 2))
    else:
        a = float(input("Versement: "))
        n = int(input("Nb echeances: "))
        if tp == 0:
            vf = a * n
        else:
            vf = a * ((1 + tp) ** n - 1) / tp
        print("Taux annuel:", round(t * 100, 4), "%")
        print("Taux", _N[p-1], round(tp * 100, 4), "%")
        print("Capital obtenu:", round(vf, 2))
        print("Total verse:", round(a * n, 2))
        print("Interets gagnes:",
              round(vf - a * n, 2))

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
    elif c == 6:
        annuite_capit()
    elif c == 0:
        break
    input("[OK]")
