print("Bienvenue sur la mini-calculatrice !")

try:
    a = float(input("Entrez le premier nombre : "))
    b = float(input("Entrez le deuxième nombre : "))
    operation = input("Choisissez une opération (+, -, *, /) : ")

    if operation == "+":
        resultat = a + b
        print("Résultat :", resultat)
    elif operation == "-":
        resultat = a - b
        print("Résultat :", resultat)
    elif operation == "*":
        resultat = a * b
        print("Résultat :", resultat)
    elif operation == "/":
        if b == 0:
            print("Erreur : division par zéro.")
        else:
            resultat = a / b
            print("Résultat :", resultat)
    else:
        print("Erreur : opération non reconnue.")

except ValueError:
    print("Erreur : veuillez entrer des nombres valides.")
