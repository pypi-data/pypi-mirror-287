import os
import sys
import platform


def write(message):
    print(message, end='')
    sys.stdout.flush()


def skipline(n=1):
    for _ in range(n):
        print()
    sys.stdout.flush()


def deleteline(n=1):
    # Move the cursor up by 'n' lines
    sys.stdout.write(f'\x1b[{n}A')
    # Erase to the end of the screen
    sys.stdout.write('\x1b[J')
    sys.stdout.flush()


def deletechar(n=1):
    sys.stdout.write(f'\x1b[{n}D')
    sys.stdout.write('\x1b[K')
    sys.stdout.flush()


def clear():
    system = platform.system()
    if system == "Windows":
        os.system('cls')
    else:
        os.system('clear')
    sys.stdout.flush()
