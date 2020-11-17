def Xsorting(inputs):
    l1=[]
    l2=[]
    for i in inputs:
        if(i[0]=='x' or i[0]=='X'):
            l1.append(i)
        else:
            l2.append(i)
    return sorted(l1)+sorted(l2)
a=['bbb', 'ccc', 'axx', 'xzz', 'xaa']
b=['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
print(Xsorting(a))
print(Xsorting(b))

