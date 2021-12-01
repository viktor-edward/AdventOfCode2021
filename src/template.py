import math


def readFile(fileInput):
    f = open(fileInput, 'r')
    data = []
    for line in f.readlines():
        data.append(str(line).replace("\n", ""))
    f.close()
    return data


def func1(data):
    
    return 0


def func2(data):
    
    return 0


def main():
    data = readFile("../resources/day2_input.txt")

    print("Part one: ")
    

    print("Part two: ")
    


if __name__ == '__main__':
    main()
