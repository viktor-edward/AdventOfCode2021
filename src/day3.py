import math


def readFile(fileInput):
    f = open(fileInput, 'r')
    data = []
    for line in f.readlines():
        data.append(str(line.replace("\n", "")))
    f.close()
    return data


def listBinaryToDec(listInput):
    decOutput = 0
    for i in range(len(listInput)):
        decOutput += pow(2, i)*listInput[-1-i]
    return decOutput


def reduceList(pos, filterList, listInput):
    newList = []
    for row in listInput:
        if row[pos] == str(filterList):
            newList.append(row)
    return newList


def calculateBitsTot(data):
    bitsTot = [0] * len(data[0])
    for row in data:
        for i in range(len(row)):
            bitsTot[i] += int(row[i])
    return bitsTot


def main():
    data = readFile("../resources/day3_input.txt")

    print("Part one: ")
    print(len(data))
    bitsTot = calculateBitsTot(data)
    gammaBinary = list(map(lambda x: 1 if x >= len(data)/2 else 0, bitsTot))
    epsilonBinary = list(map(lambda x: 1 if x == 0 else 0, gammaBinary))
    binary = listBinaryToDec(gammaBinary)
    epsilon = listBinaryToDec(epsilonBinary)
    print(binary * epsilon)

    print("Part two: ")
    pos = 0
    dataOxygen = data
    bitsTot = calculateBitsTot(dataOxygen)
    filterOxy = list(map(lambda x: 1 if x >= len(dataOxygen) / 2 else 0, bitsTot))
    while len(dataOxygen) > 1:
        dataOxygen = reduceList(pos, filterOxy[pos], dataOxygen)
        bitsTot = calculateBitsTot(dataOxygen)
        filterOxy = list(map(lambda x: 1 if x >= len(dataOxygen) / 2 else 0, bitsTot))
        pos += 1

    pos = 0
    dataScrubber = data
    bitsTot = calculateBitsTot(dataScrubber)
    filterScrubber = list(map(lambda x: 1 if x < len(dataScrubber) / 2 else 0, bitsTot))
    while len(dataScrubber) > 1:
        dataScrubber = reduceList(pos, filterScrubber[pos], dataScrubber)
        bitsTot = calculateBitsTot(dataScrubber)
        filterScrubber = list(map(lambda x: 1 if x < len(dataScrubber) / 2 else 0, bitsTot))
        pos += 1

    print(int(dataOxygen[0], 2))
    print(int(dataScrubber[0], 2))
    print(int(dataOxygen[0], 2) * (int(dataScrubber[0], 2)))


if __name__ == '__main__':
    main()
