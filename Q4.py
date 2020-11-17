def last(inputs):
    return inputs[-1]
def Sort(inputs):
    return sorted(inputs,key=last)
a=[(1, 3), (3, 2), (2, 1)]
b=[(1, 7), (1, 3), (3, 4, 5), (2, 2)]
print(Sort(a))
print(Sort(b))