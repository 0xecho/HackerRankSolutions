# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

a,b = input().split()
b = int(b)
a=sorted(a)
for i in range(b):
    l = []
    for j in combinations(a,i+1):
        l.append("".join(j))
    print(*sorted(l),sep="\n")
