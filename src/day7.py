def readFile(fileInput):
    f = open(fileInput, 'r')
    data = []
    for line in f.readlines():
        data = line.replace("\n", "").split(",")
    f.close()
    return list(map(int, data))


def main():
    data = readFile("../resources/day7_input.txt")

    print("Part one: ")
    maxLen = max(data)
    moves = []
    for pos in range(maxLen):
        moves.append(sum(map(lambda x: abs(pos - x), data)))
    print(min(moves))

    print("Part two: ")
    # Sum k, {i=1, n} = n(n+1)/2
    maxLen = max(data)
    moves = []
    for pos in range(maxLen):
        moves.append(sum(map(lambda x: abs(pos - x)*(abs(pos - x) + 1)/2, data)))
    print(min(moves))


if __name__ == '__main__':
    main()
