def readFile(fileInput):
    f = open(fileInput, 'r')
    data = ""
    for line in f.readlines():
        data = str(line).replace("\n", "")
    f.close()
    return data


def main():
    data = readFile("../resources/day17_input.txt")
    vals = data[13:].split(", ")
    xVals = vals[0][2:].split("..")
    xMin = int(xVals[0])
    xMax = int(xVals[1])
    yVals = vals[1][2:].split("..")
    yMin = int(yVals[0])
    yMax = int(yVals[1])

    print("Part one: ")
    possibleHits = []
    for yVolStart in range(-abs(yMin), abs(yMin)):
        for xVolStart in range(abs(xMax) + 1):
            yMaxInternal = 0
            x, y = 0, 0
            xVol = xVolStart
            yVol = yVolStart
            while x <= xMax and y >= yMin:
                x += xVol
                y += yVol
                if y > yMaxInternal:
                    yMaxInternal = y
                if xMin <= x <= xMax and yMin <= y <= yMax:
                    possibleHits.append([yMaxInternal, xVolStart, yVolStart])
                    break
                else:
                    if xVol > 0:
                        xVol += -1
                    yVol += -1
    maxHeight = possibleHits[0]
    for hits in possibleHits:
        if hits[0] > maxHeight[0]:
            maxHeight = hits
    print(maxHeight)

    print("Part two: ")
    print(len(possibleHits))

    


if __name__ == '__main__':
    main()
