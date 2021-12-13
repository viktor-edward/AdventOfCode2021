import numpy as np


def readFile(fileInput):
    f = open(fileInput, 'r')
    data = np.zeros((1500, 1500))
    instructions = []
    for line in f.readlines():
        if line.startswith("fold"):
            instructions.append(line[11:].replace("\n", ""))
        elif len(line) > 1:
            xtemp, ytemp = line.replace("\n", "").split(",")
            data[int(ytemp)][int(xtemp)] = 1
    f.close()
    return data, instructions


def main():
    data, instructions = readFile("../resources/day13_input.txt")

    print("Part one: ")
    for instr in instructions:
        x = instr.split("=")
        if x[0] == "x":
            for i in range(len(data)):
                for j in range(int(x[1]) + 1, len(data[0])):
                    if data[i][j] == 1:
                        data[i][2 * int(x[1]) - j] = 1
            data = data[:, :int(x[1])]
        elif x[0] == "y":
            for i in range(int(x[1]) + 1, len(data)):
                for j in range(len(data[0])):
                    if data[i][j] == 1:
                        data[2 * int(x[1]) - i][j] = 1
            data = data[:int(x[1]), :]
        break
    print(data.sum())

    print("Part two: ")
    data, instructions = readFile("../resources/day13_input.txt")
    for instr in instructions:
        x = instr.split("=")
        if x[0] == "x":
            for i in range(len(data)):
                for j in range(int(x[1]) + 1, len(data[0])):
                    if data[i][j] == 1:
                        data[i][2 * int(x[1]) - j] = 1
            data = data[:, :int(x[1])]
        elif x[0] == "y":
            for i in range(int(x[1]) + 1, len(data)):
                for j in range(len(data[0])):
                    if data[i][j] == 1:
                        data[2 * int(x[1]) - i][j] = 1
            data = data[:int(x[1]), :]
    print('\n'.join(['\t'.join(list(map(lambda y: "#" if y == 1 else ".", row))) for row in data]))


if __name__ == '__main__':
    main()
