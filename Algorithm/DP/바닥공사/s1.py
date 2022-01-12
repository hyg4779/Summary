import sys
sys.stdin = open('input.txt','r',encoding='utf-8')

n = int(input())

d = [0]* 1001

d[1] = 1
d[2] = 3

for x in range(3, n+1):
    d[x] = (d[x-1] + 2*d[x-2])%796796

print(d[n])