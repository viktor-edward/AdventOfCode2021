import math
import pandas as pd


def readFile(fileInput):
    f = open(fileInput, 'r')
    data = []
    for line in f.readlines():
        data.append(int((line).replace("\n", "")))
    f.close()
    return data


def main():
    data = readFile("../resources/day1_input.txt")

    print("Part one: ")
    print(int(pd.Series(data).rolling(window=2).apply(lambda x: x.iloc[1] - x.iloc[0] > 0).sum()))

    print("Part two: ")
    print(int(pd.Series(data).rolling(window=4).apply(lambda x: x.iloc[3] - x.iloc[0] > 0).sum()))


if __name__ == '__main__':
    main()
