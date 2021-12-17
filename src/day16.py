totalVersions = 0


def readFile(fileInput):
    f = open(fileInput, 'r')
    data = ""
    for line in f.readlines():
        data = str(line).replace("\n", "")
    f.close()
    return data


def readPacket(packet):
    global totalVersions
    value = 0
    packetVersion = int(packet[:3], 2)
    totalVersions += packetVersion
    packetType = int(packet[3:6], 2)
    if packetType == 4:
        packet = packet[6:]
        value = ""
        while True:
            value += packet[1:5]
            cnt = packet[0]
            packet = packet[5:]
            if cnt == '0':
                break
        value = int(value, 2)
    else:
        lengthType = packet[6]
        tempValues = []
        if lengthType == "0":
            bitSize = int(packet[7:22], 2)
            subPacket = packet[22:22 + bitSize]
            while subPacket:
                subPacket, value = readPacket(subPacket)
                tempValues.append(value)
            packet = packet[22 + bitSize:]
        else:
            amountPackets = int(packet[7:18], 2)
            packet = packet[18:]
            for i in range(amountPackets):
                packet, value = readPacket(packet)
                tempValues.append(value)
        if packetType == 0:
            value = sum(tempValues)
        elif packetType == 1:
            value = 1
            for val in tempValues:
                value *= val
        elif packetType == 2:
            value = min(tempValues)
        elif packetType == 3:
            value = max(tempValues)
        elif packetType == 5:
            value = 1 if tempValues[0] > tempValues[1] else 0
        elif packetType == 6:
            value = 1 if tempValues[0] < tempValues[1] else 0
        elif packetType == 7:
            value = 1 if tempValues[0] == tempValues[1] else 0

    return packet, value


def main():
    data = readFile("../resources/day16_input.txt")
    packet = str(bin(int(data, 16)))[2:].zfill(len(data) * 4)
    print("Part one: ")
    packet, value = readPacket(packet)
    print(totalVersions)

    print("Part two: ")
    print(value)


if __name__ == '__main__':
    main()
