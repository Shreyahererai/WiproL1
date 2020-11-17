def ReduceList(inputs):
    l = []
    l.append(inputs[0])
    for i in range(1, len(a)):
        if (inputs[i] != inputs[i - 1]):
            l.append(inputs[i])
    return l


a = [1, 2, 2, 3]
b = [2, 2, 3, 3, 3]
print(ReduceList(a))
print(ReduceList(b))
