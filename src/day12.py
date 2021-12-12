def readFile(fileInput):
    f = open(fileInput, 'r')
    data = {}
    for line in f.readlines():
        temp = str(line).replace("\n", "").split("-")
        if temp[0] in data:
            data[temp[0]].add(temp[1])
        else:
            data[temp[0]] = {temp[1]}
        if temp[1] in data:
            data[temp[1]].add(temp[0])
        else:
            data[temp[1]] = {temp[0]}
    f.close()
    return data


def findPaths(graph, start, end, paths, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        paths.append(path)
    else:
        for x in graph[start]:
            if x not in path or x.isupper():
                findPaths(graph, x, end, paths, path)


def findPathsPart2(graph, start, end, paths, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        paths.append(path)
    else:
        for x in graph[start]:
            if x != "start" and (path.count(x) == 0 or x.isupper()):
                findPathsPart2(graph, x, end, paths, path)
            elif x != "start" and path.count(x) == 1:
                isFirstDouble = True
                for y in path:
                    if path.count(y) > 1 and y.islower():
                        isFirstDouble = False
                if isFirstDouble:
                    findPathsPart2(graph, x, end, paths, path)


def main():
    graph = readFile("../resources/day12_input.txt")
    print("Part one: ")
    paths = []
    findPaths(graph, "start", "end", paths)
    print(len(paths))

    print("Part two: ")
    paths = []
    findPathsPart2(graph, "start", "end", paths)
    print(len(paths))


if __name__ == '__main__':
    main()
