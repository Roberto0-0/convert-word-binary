#!/usr/bin/python3
import sys
import json

def init(value):

    with open("data/data.json","r") as file:
        Ascii = json.load(file)

    data = []

    for i in Ascii:
        for k, v in enumerate(i):
            if value == v:
                while i[v] != 0:
                    data.append(i[v])
                    i[v] = i[v] / 2
                    i[v] = int(i[v])
                    if i[v] == 0:
                        break
    data.sort()
    for i in data:
        if i % 2 == 0 or i % 2 == 1:
            print(i % 2,end="")
    print("\n")

def main():
    try:
        init(sys.argv[1])
    except IndexError as err:
        return print("\033[31merror\033[m", err)
main()
