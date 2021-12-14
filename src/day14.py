import numpy as np
from collections import defaultdict


def readFile(fileInput):
    f = open(fileInput, 'r')
    startState = ""
    insertionRules = defaultdict(dict)
    firstLine = True
    for line in f.readlines():
        if firstLine:
            firstLine = False
            startState = line.replace("\n", "")
        elif len(line) > 1:
            insertionRules[line[0]][line[1]] = line.replace("\n", "")[6:]
    f.close()
    return startState, insertionRules


def readFilePart2(fileInput):
    f = open(fileInput, 'r')
    startState = defaultdict(dict)
    insertionRules = defaultdict(dict)
    firstLine = True
    for line in f.readlines():
        if firstLine:
            firstLine = False
            for i in range(len(line.replace("\n", "")) - 1):
                startState[line[i]][line[i + 1]] = newDictValue(startState, line[i], line[i + 1], 1)
        elif len(line) > 1:
            insertionRules[line[0]][line[1]] = line.replace("\n", "")[6:]
    f.close()
    return startState, insertionRules


def newDictValue(dictInput, key1, key2, value):
    if key2 in dictInput[key1]:
        return dictInput[key1][key2] + value
    return value


def main():
    state, insertionRules = readFile("../resources/day14_input.txt")

    print("Part one: ")  # Keeping part one solution for historical reasons.
    steps = 10
    for n in range(steps):
        tempState = []
        for i in range(len(state) - 1):
            tempState.append(state[i])
            if state[i + 1] in insertionRules[state[i]]:
                tempState.append(insertionRules[state[i]][state[i + 1]])
        tempState.append(state[-1])
        state = tempState
    mostCommon = max(set(state), key=state.count)
    leastCommon = min(set(state), key=state.count)
    print(str(state.count(mostCommon) - state.count(leastCommon)))
    firstChar = state[0]

    print("Part two: ")
    state, insertionRules = readFilePart2("../resources/day14_input.txt")
    steps = 40
    for n in range(steps):
        tempState = defaultdict(dict)
        for key1, x in state.items():
            for key2, val in x.items():
                if key2 in insertionRules[key1]:
                    tempState[key1][insertionRules[key1][key2]] = newDictValue(tempState, key1,
                                                                               insertionRules[key1][key2],
                                                                               state[key1][key2])
                    tempState[insertionRules[key1][key2]][key2] = newDictValue(tempState, insertionRules[key1][key2],
                                                                               key2, state[key1][key2])
                else:
                    tempState[key1][key2] = newDictValue(tempState, key1, key2, state[key1][key2])
        state = tempState

    sumPart2 = {}
    for key1, x in state.items():
        for key2, val in x.items():
            if key2 in sumPart2:
                sumPart2[key2] = sumPart2[key2] + val
            else:
                sumPart2[key2] = val
    # Note that the first character in the state is not included in the pairs
    sumPart2[firstChar] = sumPart2[firstChar] + 1
    print(sumPart2[max(sumPart2, key=sumPart2.get)] - sumPart2[min(sumPart2, key=sumPart2.get)])


if __name__ == '__main__':
    main()
