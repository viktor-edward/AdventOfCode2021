import math


def readFile(fileInput):
    f = open(fileInput, 'r')
    data = []
    for line in f.readlines():
        data.append(str(line).replace("\n", "").split(" "))
    f.close()
    return data


def move(pos, step):
    if step[0] == "forward":
        pos = pos[0] + step[1], pos[1]
    elif step[0] == "down":
        pos = pos[0], pos[1] + step[1]
    elif step[0] == "up":
        pos = pos[0], pos[1] - step[1]
    else:
        print("Incorrect step " + str(step))
    return pos


def moveAim(pos, step):
    if step[0] == "forward":
        pos = pos[0] + step[1], pos[1] + step[1] * pos[2], pos[2]
    elif step[0] == "down":
        pos = pos[0], pos[1], pos[2] + step[1]
    elif step[0] == "up":
        pos = pos[0], pos[1], pos[2] - step[1]
    else:
        print("Incorrect step " + str(step))
    return pos


def main():
    data = readFile("../resources/day2_input.txt")

    print("Part one: ")
    pos = 0, 0  # Horizontal, Depth
    for step in data:
        step[1] = int(step[1])
        pos = move(pos, step)
    print(pos[0] * pos[1])
    print(pos)

    print("Part two: ")
    pos = 0, 0, 0  # Horizontal, Depth, Aim
    for step in data:
        step[1] = int(step[1])
        pos = moveAim(pos, step)
    print(pos[0] * pos[1])
    print(pos)


if __name__ == '__main__':
    main()
