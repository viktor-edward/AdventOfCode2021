import math


def readFile(fileInput):
    f = open(fileInput, 'r')
    data = []
    for line in f.readlines():
        tempRow = []
        [tempRow.append(int(x)) for x in line.replace("\n", "")]
        data.append(tempRow)
    f.close()
    return data


def oneStep(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            state[i][j] += 1

    tempFlashes = 1
    totalFlashes = 0
    while tempFlashes != 0:
        tempFlashes = 0
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] > 9:
                    tempFlashes += 1
                    state[i][j] = 0
                    if i > 0:
                        if state[i - 1][j] != 0:
                            state[i - 1][j] += 1
                        if j > 0:
                            if state[i - 1][j - 1] != 0:
                                state[i - 1][j - 1] += 1
                        if j < len(state[i]) - 1:
                            if state[i - 1][j + 1] != 0:
                                state[i - 1][j + 1] += 1
                    if i < len(state) - 1:
                        if state[i + 1][j] != 0:
                            state[i + 1][j] += 1
                        if j > 0:
                            if state[i + 1][j - 1] != 0:
                                state[i + 1][j - 1] += 1
                        if j < len(state[i]) - 1:
                            if state[i + 1][j + 1] != 0:
                                state[i + 1][j + 1] += 1
                    if j > 0:
                        if state[i][j - 1] != 0:
                            state[i][j - 1] += 1
                    if j < len(state[i]) - 1:
                        if state[i][j + 1] != 0:
                            state[i][j + 1] += 1
        totalFlashes += tempFlashes
    return totalFlashes


def main():
    state = readFile("../resources/day11_input.txt")

    print("Part one: ")
    steps = 100
    numberOfFlashes = 0
    for i in range(steps):
        numberOfFlashes += oneStep(state)
    print(numberOfFlashes)

    print("Part two: ")
    state = readFile("../resources/day11_input.txt")
    steps = 1000
    for i in range(steps):
        x = oneStep(state)
        if x == 100:
            print("All octopus flashes at the same time in step: " + str(i + 1))
            break


if __name__ == '__main__':
    main()
