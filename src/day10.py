import math


def readFile(fileInput):
    f = open(fileInput, 'r')
    data = []
    for line in f.readlines():
        tempRow = []
        [tempRow.append(str(x)) for x in line.replace("\n", "")]
        data.append(tempRow)
    f.close()
    return data


def main():
    data = readFile("../resources/day10_input.txt")
    illegalClosings = []
    incompleteLines = []
    closingMapping = {")": "(", "]": "[", "}": "{", ">": "<"}

    print("Part one: ")
    for row in data:
        openingChars = []
        corruptLine = False
        for char in row:
            if char in ("(", "[", "{", "<"):
                openingChars.append(char)
            else:
                if openingChars[-1] == closingMapping[char]:
                    openingChars.pop()
                else:
                    corruptLine = True
                    illegalClosings.append(char)
                    break
        if not corruptLine:
            incompleteLines.append(openingChars)

    print(3 * illegalClosings.count(")") + 57 * illegalClosings.count("]")
          + 1197 * illegalClosings.count("}") + 25137 * illegalClosings.count(">"))

    print("Part two: ")
    scores = []
    scoreMap = {"(": 1, "[": 2, "{": 3, "<": 4}
    for incompleteLine in incompleteLines:
        score = 0
        while len(incompleteLine) > 0:
            char = incompleteLine.pop()
            score = score * 5 + scoreMap[char]
        scores.append(score)
    scores.sort(reverse=True)
    print(scores[math.floor(len(scores)/2)])


if __name__ == '__main__':
    main()
