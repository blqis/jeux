from turtle import *
from math import sqrt

def reverse_list_bool(l):
    b = []
    for i in range(len(l)):
        b = b + [not l[len(l)-1-i]]
    return b


def dragon(n):
    if n == 1:
        return [False]
    return dragon(n-1) + [False] + reverse_list_bool(dragon(n-1))


def afficheDragon(n):
    for i in range(len(dragon(n))):
        if dragon(n)[i] == False:
            left(90), forward(5)
        elif dragon(n)[i] == True:
            right(90), forward(5)

afficheDragon(10)