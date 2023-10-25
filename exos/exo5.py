nb = int(input("Saisissez valeure : "))

def factorielle(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

resultat = factorielle(nb)

print(resultat)

