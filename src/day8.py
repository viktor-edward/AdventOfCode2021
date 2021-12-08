def readFile(fileInput):
    f = open(fileInput, 'r')
    data = []
    for line in f.readlines():
        data.append(line.replace("\n", "").replace(" |", "").split(" "))
    f.close()
    return data


def decodeSignal(signal, message):
    signal = [set(x) for x in [x for x in signal]]

    signalsLenFive = [x for x in signal if len(x) == 5]  # len5 = 2, 3, 5
    signalsLenSix = [x for x in signal if len(x) == 6]  # len6 = 0, 6, 9
    one = [x for x in signal if len(x) == 2][0]
    four = [x for x in signal if len(x) == 4][0]
    seven = [x for x in signal if len(x) == 3][0]
    eight = [x for x in signal if len(x) == 7][0]
    three = [x for x in signalsLenFive if one & x == one][0]
    nine = three | four
    two = [x for x in signalsLenFive if len(x - nine) == 1][0]
    five = [x for x in signalsLenFive if (x != two and x != three)][0]
    six = [x for x in signalsLenSix if len(x & one) == 1][0]
    zero = [x for x in signalsLenSix if (x != six and x != nine)][0]

    decodedSignals = [zero, one, two, three, four, five, six, seven, eight, nine]

    return sum([decodedSignals.index(set(message[x])) * pow(10, 3 - x) for x in range(4)])


def main():
    data = readFile("../resources/day8_input.txt")

    print("Part one: ")
    outputSignals = []
    for row in data:
        for elem in row[10:]:
            outputSignals.append(elem)
    dataLen = [len(x) for x in outputSignals]
    dataLenCount = [dataLen.count(i) for i in range(0, 8)]
    print(dataLenCount[2] + dataLenCount[4] + dataLenCount[3] + dataLenCount[7])

    print("Part two: ")
    decodedSignalSum = 0
    for row in data:
        decodedSignalSum += decodeSignal(row[:10], row[10:])
    print(decodedSignalSum)


if __name__ == '__main__':
    main()
