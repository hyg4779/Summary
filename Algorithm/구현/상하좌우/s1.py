import sys
sys.stdin = open('input.txt')

N = int(input())
# 행렬 크기

direction = {'L': (0, -1),'R': (0, 1),'U': (-1, 0),'D': (1,0)}
# 입력별 방향

di_list = list(input().split())
# 입력받은 방향 리스트

row_cnt, col_cnt = 1, 1

for val in di_list:
    r, c = direction[val]
    if 1 <= row_cnt + r <= N and 1 <= col_cnt + c <= N:
        row_cnt += r
        col_cnt += c
        
print(row_cnt, col_cnt)