# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations
a,b=input().split()
l=[]
for i in permutations(a,int(b)):
    l.append("".join(i))
print(*sorted(l),sep="\n")
    
