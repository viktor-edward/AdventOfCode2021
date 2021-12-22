import math
import json


def readFile(fileInput):
    f = open(fileInput, 'r')
    data = list(map(json.loads, f.read().splitlines()))
    f.close()
    return data


def calcMagnitude(state):
    if isinstance(state, int):
        return state
    else:
        return 3 * calcMagnitude(state[0]) + 2 * calcMagnitude(state[1])


def explode(state, depth=1):
    if isinstance(state, int):
        return 0
    if depth == 3:
        if isinstance(state):
            return 0
    return 0


def split(state, depth=1):
    if isinstance(state, int):
        if state > 8:
            return [math.floor(state), math.ceil(state)]
    else:
        return [split(state[0]), split(state[1])]
    return 0


def main():
    data = readFile("../resources/day18_input.txt")
    state = data.pop(0)

    print("Part one: ")
    for row in data:
        state = [state, row]
        #explode(state)
        split(state)
    print(calcMagnitude(state))
    print(state)
    #print(state[1][1])


    print("Part two: ")
    


if __name__ == '__main__':
    main()
