import math
import numpy as np


def readFile(fileInput):
    f = open(fileInput, 'r')
    data = []
    for line in f.readlines():
        data.append(str(line).replace("\n", "").split(" -> "))
    f.close()
    return data


def calculateNormDirections(data):
    directions = []
    for row in data:
        xDir = int(row[0].split(",")[0]) - int(row[1].split(",")[0])
        yDir = int(row[0].split(",")[1]) - int(row[1].split(",")[1])
        xDirNorm = -int(xDir / math.sqrt(pow(xDir, 2) + pow(yDir, 2)))
        yDirNorm = -int(yDir / math.sqrt(pow(xDir, 2) + pow(yDir, 2)))
        # Ignore 0, 0 since those are not horizontal or vertical in part 1
        directions.append([xDirNorm, yDirNorm])
    return directions


def calculateNormDirectionsPart2(data):
    directions = []
    for row in data:
        xDir = int(row[0].split(",")[0]) - int(row[1].split(",")[0])
        yDir = int(row[0].split(",")[1]) - int(row[1].split(",")[1])
        xDirNorm = round(-xDir / math.sqrt(pow(xDir, 2) + pow(yDir, 2)))
        yDirNorm = round(-yDir / math.sqrt(pow(xDir, 2) + pow(yDir, 2)))
        # Ignore 0, 0 since those are not horizontal or vertical in part 1
        directions.append([xDirNorm, yDirNorm])
    return directions


def updateGrid(grid, data, directions):
    for i in range(len(data)):
        row = data[i]
        x = int(row[0].split(",")[0])
        y = int(row[0].split(",")[1])
        xEnd = int(row[1].split(",")[0])
        yEnd = int(row[1].split(",")[1])
        if not (directions[i][0] == 0 and directions[i][1] == 0):
            grid[y][x] += 1
            while not (x == xEnd and y == yEnd):
                x += directions[i][0]
                y += directions[i][1]
                grid[y][x] += 1


def main():
    data = readFile("../resources/day5_input.txt")
    gridSize = 1000

    print("Part one: ")
    grid = np.zeros((gridSize, gridSize))
    directions = calculateNormDirections(data)
    updateGrid(grid, data, directions)
    print(np.where(grid > 1, 1, 0).sum())

    print("Part two: ")
    grid = np.zeros((gridSize, gridSize))
    directions = calculateNormDirectionsPart2(data)
    updateGrid(grid, data, directions)
    print(np.where(grid > 1, 1, 0).sum())


if __name__ == '__main__':
    main()
