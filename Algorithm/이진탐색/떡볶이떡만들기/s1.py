import sys
sys.stdin = open('input.txt','r',encoding='utf-8')

N, M = map(int, input().split())
array = list(map(int, input().split()))

array.sort()

max_size = array[-1] - M
# 요청한 떡을 줄 수 있는 절단기의 최대높이

start = max_size
end = array[-1]

while start <= end:
    mid = (start + end) // 2
    result = 0
    for x in array:
        if x - mid > 0:
            result += x - mid
    if result >= M:
        start = mid + 1
    else:
        end = mid - 1
print(mid)