import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    # 행 열
    matrix = [list(map(int,input().split())) for _ in range(N)]
    # 배열

    result = 0
    for i in range(N):
        if result < min(matrix[i]):
            result = min(matrix[i])
    print(result)