import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
# 제안된 수와 나눌 수

# 2 <= N <= 100,000, 2 <= K <= 100,000, K <= N



if K >= 2:
    cnt = 0
    while N != 1:
        if N%K:
            N -= 1
            cnt += 1
            continue
        N //= K
        cnt += 1
else:
    cnt = N - 1
print(cnt)