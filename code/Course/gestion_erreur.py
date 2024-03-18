def diviseurs(a: int, b: int):
    try: 
        if b > a: 
            raise ValueError(b) # Création d'une erreur 
        print(a / b)
    except ZeroDivisionError: # Si division par zéro
        print("La division par zéro est invalide")
    except TypeError: # Si erreur de type
        print("La donnée n'est pas un nombre")
    except ValueError as second_value: # Récupération de l'erreur est de la valeur passé
        print(f"La valeur {second_value} ne doit pas être supérieur à {a}") # Envoie d'une erreur customisé
    else: # Après les try et except, passe si le code n'est pas rentré dans un except (si il n'y a pas eu d'erreurs)
        print("Division sans souci")
    finally:
        print(f"J'ai tenté la division par {b}")


diviseurs(2,2)
diviseurs(2,0)
diviseurs(2, 'test')
