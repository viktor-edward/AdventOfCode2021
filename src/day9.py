def readFile(fileInput):
    f = open(fileInput, 'r')
    data = []
    for line in f.readlines():
        tempRow = []
        [tempRow.append(int(x)) for x in line.replace("\n", "")]
        data.append(tempRow)
    f.close()
    return data


def isLowPoint(data, i, j):
    if i > 0:
        if data[i - 1][j] <= data[i][j]:
            return False
    if i < len(data) - 1:
        if data[i + 1][j] <= data[i][j]:
            return False
    if j > 0:
        if data[i][j - 1] <= data[i][j]:
            return False
    if j < len(data[i]) - 1:
        if data[i][j + 1] <= data[i][j]:
            return False
    return True


def findBasinSize(data, i, j, visitedPoints):
    visitedPoints.add((i, j))
    if i > 0 and not {i - 1, j} in visitedPoints and 9 > data[i - 1][j] > data[i][j]:
        findBasinSize(data, i - 1, j, visitedPoints)
    if i < len(data) - 1 and not {i + 1, j} in visitedPoints and 9 > data[i + 1][j] > data[i][j]:
        findBasinSize(data, i + 1, j, visitedPoints)
    if j > 0 and not {i, j - 1} in visitedPoints and 9 > data[i][j - 1] > data[i][j]:
        findBasinSize(data, i, j - 1, visitedPoints)
    if j < len(data[i]) - 1 and not {i, j + 1} in visitedPoints and 9 > data[i][j + 1] > data[i][j]:
        findBasinSize(data, i, j + 1, visitedPoints)
    return len(visitedPoints)


def main():
    data = readFile("../resources/day9_input.txt")

    print("Part one: ")
    riskLevels = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if isLowPoint(data, i, j):
                riskLevels += data[i][j] + 1
    print(riskLevels)

    print("Part two: ")
    basinSizes = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if isLowPoint(data, i, j):
                visitedPoints = set()
                basinSizes.append(findBasinSize(data, i, j, visitedPoints))
    basinSizes.sort(reverse=True)
    print(basinSizes[0] * basinSizes[1] * basinSizes[2])


if __name__ == '__main__':
    main()
