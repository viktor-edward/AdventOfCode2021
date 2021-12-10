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

    print("Part one: ")
    for row in data:
        openingChars = []
        corruptLine = False
        for char in row:
            if char in ("(", "[", "{", "<"):
                openingChars.append(char)
            else:
                if char == ")" and openingChars[-1] == "(":
                    openingChars.pop()
                elif char == "]" and openingChars[-1] == "[":
                    openingChars.pop()
                elif char == "}" and openingChars[-1] == "{":
                    openingChars.pop()
                elif char == ">" and openingChars[-1] == "<":
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
    for incompleteLine in incompleteLines:
        score = 0
        while len(incompleteLine) > 0:
            char = incompleteLine.pop()
            if char == "(":
                score = score * 5 + 1
            elif char == "[":
                score = score * 5 + 2
            elif char == "{":
                score = score * 5 + 3
            elif char == "<":
                score = score * 5 + 4
        scores.append(score)
    scores.sort(reverse=True)
    print(scores)
    print(scores[math.floor(len(scores)/2)])


if __name__ == '__main__':
    main()
