import math
import itertools as it

def readFile(fileInput):
    f = open(fileInput, 'r')
    data = []
    for line in f.readlines():
        data.append(int((line).replace("\n", "")))
    f.close()
    return data


def func1(data):
    
    return 0


def func2(data):
    
    return 0


def main():
    data = readFile("../resources/day1_input.txt")

    print("Part one: ")
    incr = 0
    for i in range(len(data)-1):
        if data[i] - data[i+1] < 0:
            incr += 1
    print(incr)

    x = it.windowed(data, 2)
    print(x)

    print("Part two: ")
    incr = 0
    for i in range(len(data)-3):
        if data[i] - data[i+3] < 0:
            incr += 1
    print(incr)


if __name__ == '__main__':
    main()
