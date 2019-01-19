from random import randint
from random import seed
from time import sleep
from time import time
from sys import platform
import os
print("Enter sizes of field")
n, m = list(map(int, input().split()))
#print("Do you use 'Windows'?(Yes|No)")
#answer = input()
#answer = answer.lower()
#if (answer == "yes" or answer == 'i do' or answer == 'y' or answer == 'yes, i do'):
#    system = "windows"
#else:
#    system = 'linux'
#if (platform == 'win32'):
#    system = 'windows'
#else:
#    system = '-'
a = [[1] * (n + 2) for i in range(m + 2)]
b = [[1] * (n + 2) for i in range(m + 2)]
seed = time()
for i in range(1, n + 1):
    for j in range(1, m + 1):
        a[i][j] = randint(0, 3)

while True:
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cou_neigh_fish = 0
            cou_neigh_shrimp = 0
            for di in range(-1, 2):
                for dj in range(-1, 2):
                     if di != 0 or dj != 0:
                        if a[i + di][j + dj] == 3:
                            cou_neigh_fish += 1
                        if a[i + di][j + dj] == 2:
                            cou_neigh_shrimp += 1
            if a[i][j] == 1:
                b[i][j] = 1
            elif a[i][j] == 3:
                if cou_neigh_fish < 2 or cou_neigh_fish >= 4:
                    b[i][j] = 0
                else:
                    b[i][j] = 3
            elif a[i][j] == 2:
                if cou_neigh_shrimp < 2 or cou_neigh_shrimp >= 4:
                    b[i][j] = 0
                else:
                    b[i][j] = 2
            else:
                if cou_neigh_fish == 3:
                    b[i][j] = 3
                elif cou_neigh_shrimp == 3:
                    b[i][j] = 2
    changing = 0
    for i in range(n + 2):
        for j in range(m + 2):
            if (a[i][j] != b[i][j]):
                changing = 1
            a[i][j] = b[i][j]
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')
    symb = [0] * 4
    symb[0] = ' '
    symb[1] = '#'
    symb[2] = '@'
    symb[3] = '~'
    print("'#' means rock")
    print("'@' means shrimp")
    print("'~' means fish")
    for i in range(n + 2):
        for j in range(m + 2):
            print(symb[a[i][j]], end='')
        print()
    if (changing == 0):
        print("Life doesn't change anymore.")
        break
    sleep(1)
