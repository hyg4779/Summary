import sys
sys.stdin = open('input.txt','r',encoding='utf-8')

T = int(input())

score = [list(input().split()) for _ in range(T)]

for i in range(len(score)-1, 0, -1):
    for j in range(1, i):
        if int(score[j][1]) < int(score[j+1][1]):
            score[j], score[j+1] = score[j+1], score[j]

print(score)