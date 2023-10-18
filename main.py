import random
import words


def test_number():
    chosen_word = int(random.randint(1, len(words.word_list)))

    if 1 < chosen_word > 4:
        print("Donnez un nombre valide")
        test_number()
    else:
        answer = int(input("Choisissez un nombre qui correspond au mot choisi"))
        if answer == chosen_word:
            print("Wouhou c'est gagné")
        else:
            print("raté")
            answer = int(input("Choisissez un autre nombre, une chance restante"))
            if answer != chosen_word:
                print("C'est perdu!")


"""
demander à l'user un nombre entre 1 et nombre elements du tableau'
choisir un mot et demandé à user de le deviner
et lui dire si ce mot est le bon
"""

test_number()
