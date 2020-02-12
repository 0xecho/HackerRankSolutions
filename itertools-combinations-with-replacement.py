# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

a,b = input().split()
for i in sorted(["".join(sorted(x)) for x in combinations_with_replacement(a,int(b))]):
    print(*i,sep="")
