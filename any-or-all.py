input()
a=input().split()
print(any([i==i[::-1] for i in a])and all([int(i)>0 for i in a]))
