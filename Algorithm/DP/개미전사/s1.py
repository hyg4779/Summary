import sys
sys.stdin = open('input.txt','r',encoding='utf-8')

N = int(input())
store = list(map(int, input().split()))

d = [0]*(N+1)

d[0] = store[0]
for i in range(2, N):
    d[i] = max(d[i-1], d[i-2]+store[i])