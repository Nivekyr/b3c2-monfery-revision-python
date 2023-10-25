n1 = int(input("Saisissez une première valeure : "))
n2 = int(input("Saisissez une deuxième valeure : "))
ope = input("Saisissez un opérateur pour le calcul : (-, +, /, *) ")

def addition(nb1, nb2):
    print(nb1 + nb2)

def substraction(nb1, nb2):
    print(nb1 - nb2)

def division(nb1, nb2):
    print(nb1 / nb2)

def multiplication(nb1, nb2):
    print(nb1 * nb2)
    
if ope == "-":
    substraction(n1, n2)
elif ope == "+":
    addition(n1, n2)
elif ope == "/":
    division(n1, n2)
elif ope == "*":
    multiplication(n1, n2)