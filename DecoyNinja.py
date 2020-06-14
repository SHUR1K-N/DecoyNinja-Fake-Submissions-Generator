import random; import os; import time
from colorama import init
from termcolor import colored

loopFlagExp = 0; loopFlagAssign = 0
expNum = 1; assignNum = 1; assign = 0; exp = 0
decisionMade = False


init()

print(colored('''
                    ▓█████▄ ▓█████  ▄████▄   ▒█████ ▓██   ██▓ ███▄    █  ██▓ ███▄    █  ▄▄▄██▀▀▀▄▄▄
                    ▒██▀ ██▌▓█   ▀ ▒██▀ ▀█  ▒██▒  ██▒▒██  ██▒ ██ ▀█   █ ▓██▒ ██ ▀█   █    ▒██  ▒████▄
                    ░██   █▌▒███   ▒▓█    ▄ ▒██░  ██▒ ▒██ ██░▓██  ▀█ ██▒▒██▒▓██  ▀█ ██▒   ░██  ▒██  ▀█▄
                    ░▓█▄   ▌▒▓█  ▄ ▒▓▓▄ ▄██▒▒██   ██░ ░ ▐██▓░▓██▒  ▐▌██▒░██░▓██▒  ▐▌██▒▓██▄██▓ ░██▄▄▄▄██
                    ░▒████▓ ░▒████▒▒ ▓███▀ ░░ ████▓▒░ ░ ██▒▓░▒██░   ▓██░░██░▒██░   ▓██░ ▓███▒   ▓█   ▓██▒
                     ▒▒▓  ▒ ░░ ▒░ ░░ ░▒ ▒  ░░ ▒░▒░▒░   ██▒▒▒ ░ ▒░   ▒ ▒ ░▓  ░ ▒░   ▒ ▒  ▒▓▒▒░   ▒▒   ▓▒█░
                     ░ ▒  ▒  ░ ░  ░  ░  ▒     ░ ▒ ▒░ ▓██ ░▒░ ░ ░░   ░ ▒░ ▒ ░░ ░░   ░ ▒░ ▒ ░▒░    ▒   ▒▒ ░
                     ░ ░  ░    ░   ░        ░ ░ ░ ▒  ▒ ▒ ░░     ░   ░ ░  ▒ ░   ░   ░ ░  ░ ░ ░    ░   ▒
                       ░       ░  ░░ ░          ░ ░  ░ ░              ░  ░           ░  ░   ░        ░  ░
                     ░             ░                 ░ ░                                                 ''', 'blue'))
print(colored('''                                               DecoyNinja: The Decoy Generator''', 'red'))
print(colored('''                                         -------------------------------------------''', 'blue'))


def promptAssign(assign):
    while (decisionMade is False):
        assign = str(input("Enter the number of assignments to decoy (Default = 1): ") or "1")
        try:
            assign = int(assign)
            break
        except:
            print("\nInvalid entry. Enter an integer. Try again.\n")
            assign = 0
            continue
    return (assign)


def promptExp(exp):
    while (decisionMade is False):
        exp = str(input("Enter the number of experiments to decoy (Default = 1): ") or "1")
        try:
            exp = int(exp)
            break
        except:
            print("\nInvalid entry. Enter an integer. Try again.\n")
            exp = 0
            continue
    return (exp)


########## Main ##########

assign = promptAssign(assign)
exp = promptExp(exp)

Output = str(input("Enter output folder (Default = current folder):") or "./")
Output += "/"
OutputCopy = Output

print("\nWorking...", end='')

start = time.time()
while (loopFlagExp < exp):
    Output += "Experiment (%d).pdf" % expNum
    if (exp != 0):
        with open(Output, '+w') as file:
            randmFill = random.randint(500000, 1000000)
            choices = ['å', '¼', 'Ü', '€', '´', 'W', '', '„', ' ', 'ñ', '”', 'Ó', 'l', 'D', '/', '‘', 'N', 'œ', '¦', 'l', 'ž', '£', ']', 'ß', '6', 'T', '1', 'Š', 'ï', '', 'õ', 'F', 'N', '‰', 'Î', '&', ';', '?', '#', '^', 'q', '%', ' ', '~', ':', 'k', '2', '±', '¼', 'l', ' ', 'X', 'r', '0', 'm', '*', '(', '@', '$', '?', '7', '.', 'j', '+', ',']
            for i in range(0, randmFill):
                file.write(random.choice(choices))
        file.close()
        loopFlagExp += 1
        expNum += 1
        Output = OutputCopy
    else:
        break

while (loopFlagAssign < assign):
    Output += "Assignment (%d).pdf" % assignNum
    if (assign != 0):
        with open(Output, '+w') as file:
            randmFill = random.randint(600000, 1000000)
            choices = ['%', ' ', '[', '~', ':', 'k', '0', '2', '±', '¼', 'h', ' ', '-', 'Q', '_', '', 'u', '.', '3', 'L', 'f', '', 'å', 'j', 'Ü', '€', '´', ' ', 'i', 'ž', '£', ']', 'ß', '6', 'T', '1', 'Š', 'ï', ' ', 'õ', 'm', 'o', '‰', 'P', '', 'ñ', '”', 'Ó', 'l', 'ð', ' ', '‘', 'N', 'œ', '¦', 'Î', '&', ';', '?', '#', '^', 'q', '—']
            for i in range(0, randmFill):
                file.write(random.choice(choices))
        file.close()
        loopFlagAssign += 1
        assignNum += 1
        Output = OutputCopy
    else:
        break

completionTime = time.time() - start

print("\n\nThe task completed successfully in %f seconds." % completionTime)
print("Press any key to exit. GG;WP.")
secret = input()
os.sys.exit()
