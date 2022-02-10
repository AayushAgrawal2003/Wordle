a_file = open("words.txt", "r")
import random
words = [(line.strip()) for line in a_file]
a_file.close()
c = 1
import colorama
from colorama import Fore,Style,Back
#choose a word s
#ans = words[random.randint(0,len(words))]
ans = 'print'
def guess_input(c):
    n = str(input("Enter Guess " + str(c) + "\n")).lower().strip()
    if len(n) != 5:
        print("5 letters only")
        n = guess_input(c)
    if n not in words:
        print("not recognized")
        n = guess_input(c)
    return str(n)


def play(guess,c):
    if guess == ans:
        return "WINNER!!!"
    elif c == 6:
        print(Fore.GREEN + ans)
        return "GAME OVER"
    else:
        ret = []
        n_guess = list(guess)
        n_ans = list(ans)
        for i in range(5):
            if n_ans[i] == n_guess[i]:
                ret.append(Fore.GREEN + n_guess[i])
            elif n_guess[i] in n_ans:
                ret.append(Fore.YELLOW + n_guess[i])
            else:
                ret.append(Style.RESET_ALL + n_guess[i])
        ret.append(Style.RESET_ALL)
        print(" ".join(ret))
        c+=1
        return play(guess_input(c),c)

print(Fore.RED + Back.GREEN + play(guess_input(c),c))

