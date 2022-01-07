import sys
sys.stdin = open('input.txt')
"""
N, M, K = map(int, input().split())
# 배열크기, 더할 횟수, 한 인덱스당 연속 연산 가능 횟수

nums = sorted(list(map(int, input().split())))
nums_index = [0]*len(nums)
# 구분할 인덱스

result = 0
# 최종 답

cnt = 0
# 더한 횟수

while cnt < M:
    if nums_index[-1] == K:
        result += nums[-2]
        nums_index[-1] = 0
    else:
        result += nums[-1]
        nums_index[-1] += 1
    cnt += 1
print(result)
"""
N, M, K = map(int, input().split())
# 배열크기, 더할 횟수, 한 인덱스당 연속 연산 가능 횟수

nums = sorted(list(map(int, input().split())))
# 배열

first = nums[-1]
second = nums[-2]

result = (M//(K+1))*(first*K + second)
result += (M%(K+1))*first
print(result)