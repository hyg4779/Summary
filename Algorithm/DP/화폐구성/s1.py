import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N, M = map(int,input().split())
    # 화폐 개수, 목표 금액

    coin_list = [int(input()) for _ in range(N)]
    # 화폐 종류 리스트

    d = [10001]*(M+1)
    d[0] = 0
    for i in range(N):
        for j in range(coin_list[i], M+1):
            if d[j-coin_list[i]] != 10001:
                d[j] = min(d[j], d[j-coin_list[i]]+1)

    if d[M] == 10001:
        print(-1)
    else:
        print(d[M])

    