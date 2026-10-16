from ft_filter import ft_filter
import sys

def main():
    """filterstring.py: filter string by length of words"""
    try:
        if (len(sys.argv) != 3):
            raise AssertionError("the arguments are bad")

        arg1 = sys.argv[1]

        try:
            arg2 = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        # if (arg1 == "None"):
        #     raise AssertionError("the arguments are bad")

        result = [char for char in ft_filter(lambda x: len(x) > arg2, arg1.split())]


        print(result)

    except AssertionError as error:
        print(f"AssertionError: {error}")

if __name__ == "__main__":
    main()

# Notes random
'''
lambda x: len(x) > arg2 = fonction anonyme (jetable) qui prend x en paramètre et retourne True si sa taille est > arg2
arg1.split() = découpe une chaîne de caractères en une liste de mots (utilise l'espace comme séparateur par défaut)
[mot for mot in ft_filter(...)] = syntaxe de liste en compréhension exigée pour construire le tableau final
raise AssertionError = déclenche manuellement une exception pour interrompre le flux et sauter au bloc except
try / except ValueError = permet de tester la conversion int() sans faire crasher le programme si l'utilisateur tape du texte
'''