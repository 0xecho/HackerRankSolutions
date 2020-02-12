cube = lambda x:x**3
def fibonacci(n):
    l=[0]
    if n==0:
        l=[]
    if n>1:
        l.append(1)
    
    for i in range(n-2):
        l.append(l[-1]+l[-2])
    return l
