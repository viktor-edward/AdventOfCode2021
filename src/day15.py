from queue import PriorityQueue
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


def findShortestPath(data):
    nodesBestScore = {}
    for i in range(len(data)):
        for j in range(len(data[i])):
            nodesBestScore[(i, j)] = math.inf
    nodesBestScore[(0, 0)] = 0
    q = PriorityQueue()
    q.put((0, (0, 1)))
    q.put((0, (1, 0)))
    paths = []

    while not q.empty():
        cost, pos = q.get()
        x, y = pos[0], pos[1]
        if pos in nodesBestScore and cost + data[y][x] < nodesBestScore[pos]:
            cost += data[y][x]
            nodesBestScore[(x, y)] = cost
            if x == len(data) - 1 and y == len(data[0]) - 1:
                paths.append((cost, pos))
            else:
                q.put((cost, (x + 1, y)))
                q.put((cost, (x - 1, y)))
                q.put((cost, (x, y + 1)))
                q.put((cost, (x, y - 1)))
    return paths


def main():
    data = readFile("../resources/day15_input.txt")

    print("Part one: ")
    paths = findShortestPath(data)
    print(paths)

    print("Part two: ")
    resizeFactor = 5
    mapPart2 = []
    for i in range(resizeFactor):
        for row in data:
            tempRow = []
            for j in range(resizeFactor):
                for s in row:
                    tempRow.append((s + i + j) % 10 + math.floor((s + i + j)/10))  # Ugly hack, not working for N > 10
            mapPart2.append(tempRow)
    paths = findShortestPath(mapPart2)
    print(paths)


if __name__ == '__main__':
    main()
