def CountString(inputs):
    c=0
    for i in inputs:
        if(i[0]==i[-1] and len(i)>=2):
            c=c+1
    return c
a=['axa', 'xyz', 'gg', 'x', 'yyy']
b=['x', 'cd', 'cnc', 'kk']
c=['bab', 'ce', 'cba', 'syanora']
print(CountString(a))
print(CountString(b))
print(CountString(c))

