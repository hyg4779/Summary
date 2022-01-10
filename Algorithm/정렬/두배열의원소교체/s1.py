import sys
sys.stdin = open('input.txt','r',encoding='utf-8')

N, K = map(int, input().split())

nums_a = list(map(int, input().split()))
nums_b = list(map(int, input().split()))

def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left < right:
        while left <= end and array[left] < pivot:
            left += 1

        while right > left and array[right] >= pivot:
            right -= 1

        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)



def quick_sort_2(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort_2(left) + [pivot] + quick_sort_2(right) 

nums_b = quick_sort_2(nums_b)

nums_b = nums_b[::-1]
for i in range(K):
    nums_a[i], nums_b[i] = nums_b[i], nums_a[i]

print(nums_a)
print(sum(nums_a))