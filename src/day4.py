import math
from copy import deepcopy

bingoSize = 5


def readFile(fileInput):
    f = open(fileInput, 'r')
    data = []
    for line in f.readlines():
        row = str(line).replace("\n", "").split()
        if row:
            data.append(row)
    f.close()
    return data


def createBingoMatrices(data):
    i = 0
    bingoMatrices = []
    tempMatrix = []
    for row in data:
        tempMatrix.append(row)
        if i == bingoSize - 1:
            i = 0
            bingoMatrices.append(tempMatrix)
            tempMatrix = []
        else:
            i += 1
    return bingoMatrices


def playBingo(number, bingoMatrices):
    i = 0
    for bingo in bingoMatrices:
        for row in bingo:
            for element in row:
                if element == number:
                    row[i] = "x"
                i += 1
            i = 0


def checkBingo(bingoMatrices):
    # Check rows
    for k in range(len(bingoMatrices)):
        for i in range(bingoSize):
            for j in range(bingoSize):
                if bingoMatrices[k][i][j] != "x":
                    break
                elif j == 4:
                    return True, k

    # Check columns
    for k in range(len(bingoMatrices)):
        i, j = 0, 0
        for j in range(bingoSize):
            for i in range(bingoSize):
                if bingoMatrices[k][i][j] != "x":
                    break
                elif i == 4:
                    return True, k
    return False, 0


def checkBingoPartTwo(bingoMatrices, bingos, round):
    # Check rows
    for k in range(len(bingoMatrices)):
        for i in range(bingoSize):
            for j in range(bingoSize):
                if bingoMatrices[k][i][j] != "x":
                    break
                elif j == 4:
                    if bingos[k] == -1:
                        bingos[k] = round

    # Check columns
    for k in range(len(bingoMatrices)):
        i, j = 0, 0
        for j in range(bingoSize):
            for i in range(bingoSize):
                if bingoMatrices[k][i][j] != "x":
                    break
                elif i == 4:
                    if bingos[k] == -1:
                        bingos[k] = round


def calcNonMarkedSum(bingoMatrix):
    sumTot = 0
    for row in bingoMatrix:
        for element in row:
            if element != "x":
                sumTot += int(element)
    return sumTot


def main():
    data = readFile("../resources/day4_input.txt")
    numbers = data[0][0].split(",")
    orgBingoMatrices = createBingoMatrices(data[1:])
    bingoMatrices = deepcopy(orgBingoMatrices)

    print("Part one: ")
    for number in numbers:
        playBingo(number, bingoMatrices)
        bingo, bingoIndex = checkBingo(bingoMatrices)
        if bingo:
            print("BINGO")
            print(calcNonMarkedSum(bingoMatrices[bingoIndex]))
            print(calcNonMarkedSum(bingoMatrices[bingoIndex]) * int(number))
            break

    print("Part two: ")
    bingoMatrices = deepcopy(orgBingoMatrices)
    bingos = [-1] * len(bingoMatrices)
    round = 0
    for number in numbers:
        playBingo(number, bingoMatrices)
        checkBingoPartTwo(bingoMatrices, bingos, round)
        if -1 not in bingos:
            print("Last bing found.")
            maxValue = max(bingos)
            maxIndex = bingos.index(maxValue)
            print(calcNonMarkedSum(bingoMatrices[maxIndex]) * int(number))
            break
        round += 1
    print(bingos)


if __name__ == '__main__':
    main()
