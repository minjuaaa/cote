#메모리 제한 주의해야함
# 한 줄 입력 -> 정렬 - 자르기 -> 한 줄 입력 -> 반복

n = int(input())
arr = []

for _ in range(n):
    new = list(map(int,input().split()))
    arr = arr + new
    arr.sort(reverse=True)

    arr = arr[0:n]

print(arr[n-1])