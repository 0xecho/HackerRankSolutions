# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

a = [int(i)for i in input().split()]
b = [int(i)for i in input().split()]

print(*product(a,b))
