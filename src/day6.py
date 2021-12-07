import math
from copy import deepcopy
import numpy as np


def readFile(fileInput):
    f = open(fileInput, 'r')
    data = []
    for line in f.readlines():
        data = line.replace("\n", "").split(",")
    f.close()
    return list(map(int, data))


def stepOneDay(fish):
    for i in range(len(fish)):
        if fish[i] == 0:
            fish[i] = 6
            fish.append(8)
        else:
            fish[i] += -1


def stepOneDayPart2(fish):
    temp = fish.pop(0)
    fish.append(temp)
    fish[6] += temp


def main():
    fish = readFile("../resources/day6_input.txt")
    fishPart2 = deepcopy(fish)

    print("Part one: ")
    steps = 80
    for i in range(steps):
        stepOneDay(fish)
    print(len(fish))

    print("Part two: ")
    steps = 256
    # Instead of keeping track of all fish keep track of how many there are in each stage
    fish = list(np.zeros(9))
    for fishIndex in fishPart2:
        fish[fishIndex] += 1
    for i in range(steps):
        stepOneDayPart2(fish)
    print(sum(fish))


if __name__ == '__main__':
    main()
