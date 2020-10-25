import time; import os
import threading; import random
from termcolor import colored
import colorama

colorama.init()

loopFlagAssign = 0; loopFlagExp = 0
expNum = 1; assignNum = 1

BANNER1 = colored('''
                ▓█████▄ ▓█████  ▄████▄   ▒█████ ▓██   ██▓ ███▄    █  ██▓ ███▄    █  ▄▄▄██▀▀▀▄▄▄
                ▒██▀ ██▌▓█   ▀ ▒██▀ ▀█  ▒██▒  ██▒▒██  ██▒ ██ ▀█   █ ▓██▒ ██ ▀█   █    ▒██  ▒████▄
                ░██   █▌▒███   ▒▓█    ▄ ▒██░  ██▒ ▒██ ██░▓██  ▀█ ██▒▒██▒▓██  ▀█ ██▒   ░██  ▒██  ▀█▄
                ░▓█▄   ▌▒▓█  ▄ ▒▓▓▄ ▄██▒▒██   ██░ ░ ▐██▓░▓██▒  ▐▌██▒░██░▓██▒  ▐▌██▒▓██▄██▓ ░██▄▄▄▄██
                ░▒████▓ ░▒████▒▒ ▓███▀ ░░ ████▓▒░ ░ ██▒▓░▒██░   ▓██░░██░▒██░   ▓██░ ▓███▒   ▓█   ▓██▒
                 ▒▒▓  ▒ ░░ ▒░ ░░ ░▒ ▒  ░░ ▒░▒░▒░   ██▒▒▒ ░ ▒░   ▒ ▒ ░▓  ░ ▒░   ▒ ▒  ▒▓▒▒░   ▒▒   ▓▒█░
                 ░ ▒  ▒  ░ ░  ░  ░  ▒     ░ ▒ ▒░ ▓██ ░▒░ ░ ░░   ░ ▒░ ▒ ░░ ░░   ░ ▒░ ▒ ░▒░    ▒   ▒▒ ░
                 ░ ░  ░    ░   ░        ░ ░ ░ ▒  ▒ ▒ ░░     ░   ░ ░  ▒ ░   ░   ░ ░  ░ ░ ░    ░   ▒
                   ░       ░  ░░ ░          ░ ░  ░ ░              ░  ░           ░  ░   ░        ░  ░
                 ░             ░                 ░ ░''', 'blue')
BANNER2 = colored('''                                     DecoyNinja: The Decoy Submissions Generator''', 'red')
BANNER3 = colored('''                                     -------------------------------------------''', 'blue')


def printBanner():
    print(BANNER1), print(BANNER2), print(BANNER3)


def generateExps(outputPath, loopFlagExp, expNum):
    while (loopFlagExp < exp):
        outputPath += f"Experiment {expNum}.pdf"
        if (exp != 0):
            with open(outputPath, "wb") as file:
                randomLength = random.randint(500000, 1000000)
                file.write(os.urandom(randomLength))
            loopFlagExp += 1; expNum += 1
            outputPath = resetPath
        else:
            break


def generateAssigns(outputPath, loopFlagAssign, assignNum):
    while (loopFlagAssign < assign):
        outputPath += f"Assignment {assignNum}.pdf"
        if (assign != 0):
            with open(outputPath, "wb") as file:
                randomLength = random.randint(600000, 1000000)
                file.write(os.urandom(randomLength))
            loopFlagAssign += 1; assignNum += 1
            outputPath = resetPath
        else:
            break


def clrscr():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
    printBanner()


############### Main ###############

if __name__ == "__main__":

    printBanner()

    try:

        while (True):
            try:
                assign = int(input("\nEnter the number of assignments to decoy (Default = 1): ") or 1)
                exp = int(input("Enter the number of experiments to decoy (Default = 1): ") or 1)
                break
            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except:
                clrscr()
                print("Invalid entry. Enter an integer. Try again.\n")
                continue

        while (True):
                outputPath = str(input("Enter output folder (Default = current folder):") or "./")
                outputPath += "/"
                resetPath = outputPath

                if (os.path.exists(outputPath) is True):
                    break
                else:
                    clrscr()
                    print("Either file does not exist or invalid path entered. Try again.\n")
                    continue

        threadExps = threading.Thread(target=generateExps, args=[outputPath, loopFlagExp, expNum])
        threadAssigns = threading.Thread(target=generateAssigns, args=[outputPath, loopFlagAssign, assignNum])

        clrscr()
        print("\nWorking...", end='')

        start = time.time()

        threadExps.start()
        threadAssigns.start()

        threadExps.join()
        threadAssigns.join()

        completionTime = time.time() - start

        clrscr()
        print(f"\nThe task completed successfully in {completionTime} seconds.")
        print("Press Enter to exit. GG;WP.")
        input()

    except KeyboardInterrupt:
        clrscr()
        print("\nCTRL ^C\n\nThrew a wrench in the works.")
        print("Press Enter to exit.")
        input()
