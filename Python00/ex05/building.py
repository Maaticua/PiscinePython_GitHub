import sys


def main():
    """ fonction qui compte les types de char dans une chaine """
    try:
        if len(sys.argv) < 2 or sys.argv[1] == "":
            print("What is the text to count?")
            mstr = sys.stdin.readline()
        elif (len(sys.argv) > 2):
            raise AssertionError("more than one argument is provided")
        else:
            mstr = sys.argv[1]

        str_len = len(mstr)
        print(f"The text contains {str_len} characters:")

        ponctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

        upper = sum(1 for char in mstr if char.isupper())
        lower = sum(1 for char in mstr if char.islower())
        ponct = sum(1 for char in mstr if char in ponctuation)
        space = sum(1 for char in mstr if char.isspace())
        digit = sum(1 for char in mstr if char.isdigit())
        print(f"{upper} upper letters")
        print(f"{lower} lower letters")
        print(f"{ponct} punctuation marks")
        print(f"{space} spaces")
        print(f"{digit} digits")

    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(f"AssertionError: {error}")

# ranodm notes
'''
flake8 = norminette for python
main = need from now, check this ex for reference
sys.stdin.readline() = read a line from standard input (keyboard)
'''
