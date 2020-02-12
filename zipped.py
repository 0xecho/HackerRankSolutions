# Enter your code here. Read input from STDIN. Print output to STDOUT
n,k = [int(i)for i in input().split()]
l=[]
for i in range(k):
    l.append([float(j)for j in input().split()])

for i in zip(*l):
    print(sum(i)/len(i))
