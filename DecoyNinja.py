import time; import os
import threading; import random
from termcolor import colored
import colorama

colorama.init()

loopFlag = 0; decoyIter = 1

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
BANNER2 = colored('''                  ----------------------------------------------------''', 'blue')
BANNER3 = colored('''                  || DecoyNinja: The Fake PDF Submissions Generator ||''', 'red')
BANNER4 = colored('''                  ----------------------------------------------------''', 'blue')


def printBanner():
    print(BANNER1), print(BANNER2), print(BANNER3), print(BANNER4)


def header(file, randomLength):
    with open(file, "w") as file:
        file.write(f'''
%PDF-1.{random.randrange(4, 7, 1)}
%áéëÓ
{random.randrange(2, 20, 1)} 0 obj
<</Type /Catalog
/Pages
/Dests
>>
endobj
{random.randrange(1, 20, 1)} 0 obj
<</Type /Page
/Parent 1 0 R
/Resources <</ExtGState <</G0 {random.randrange(2, 10, 1)} 0 R
/G1 {random.randrange(2, 20, 1)} 0 R
/G2 {random.randrange(2, 20, 1)} 0 R
/G3 {random.randrange(2, 20, 1)} 0 R
/G4 {random.randrange(2, 20, 1)} 0 R
>>
/Font <</F0 {random.randrange(2, 20, 1)} 0 R
/F1 {random.randrange(2, 20, 1)} 0 R
>>
>>
/MediaBox [{random.randrange(0, 500, 1)} {random.randrange(0, 500, 1)} {random.randrange(2, 1000, 1)} {random.randrange(2, 1000, 1)}]
/Contents {random.randrange(2, 20, 1)} 0 R
>>
endobj
{random.randrange(2, 20, 1)} 0 obj
<</Filter /FlateDecode
/Length {randomLength}
>> stream
''')


def generateDecoy(outputPath, loopFlag, decoyIter):
    while (loopFlag < decoyNum):
        if (decoyNum == 1):
            outputPath += f"{decoyName}.pdf"
        else:
            outputPath += f"{decoyName} ({decoyIter}).pdf"
        if (decoyIter != 0):
            randomLength = random.randint(600000, 1000000)
            header(outputPath, randomLength)
            with open(outputPath, "ab") as file:
                file.write(os.urandom(randomLength))
            loopFlag += 1; decoyIter += 1
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
                decoyNum = int(input("\nEnter the number of PDFs to generate (Default = 1): ") or 1)
                if (decoyNum < 1):
                    raise Exception
                break
            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except:
                clrscr()
                print("\nInvalid entry. Enter a positive integer. Try again.\n")
                continue

        decoyName = input("Enter the name of PDF files (will automatically be numbered): ") or "Decoy"

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

        threadPool = []

        for i in range(decoyNum):
            threadPool.append(threading.Thread(target=generateDecoy, args=[outputPath, loopFlag, decoyIter]))

        clrscr()
        print("\nWorking...", end='')

        start = time.time()

        for thread in threadPool:
            thread.start()

        for thread in threadPool:
            thread.join()

        completionTime = time.time() - start

        # clrscr()
        print(f" The task completed successfully in {completionTime} seconds.")
        print("Press Enter to exit. GG;WP.")
        input()

    except KeyboardInterrupt:
        clrscr()
        print("\nCTRL ^C\n\nThrew a wrench in the works.")
        print("Press Enter to exit.")
        input()
