def Count(n):
    c=0
    i=1
    if(n>0):
        sum=0
        while sum<n:
            if(sum+i>n):
                sum=sum-i
            else:
                sum=sum+i
            i+=1
            c+=1
        print(c)
    if(n<0):
        sum=0
        while sum>n:
            if(sum-i<n):
                sum+=i
            else:
                sum=sum-i
            i+=1
            c+=1
        print(c)
n1=100000000
n2=-100000000
Count(n1)
Count(n2)