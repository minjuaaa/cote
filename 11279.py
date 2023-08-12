# 맨 처음 구현한 코드
import heapq
arr = []
heapq.heapify(arr)
tc = int(input())

for _ in range(tc):
    now = int(input())

    if now == 0:
        if (len(arr)) == 0:
            print(0)

        else:
            print(arr[-1])
            del arr[-1]

    else:
        heapq.heappush(arr, now)


#틀려서 수정
import heapq
import sys

arr = []
heapq.heapify(arr)
tc = int(sys.stdin.readline())

for _ in range(tc):
    now = int(sys.stdin.readline())

    if now == 0:
        if (len(arr)) == 0:
            print(0)

        else:
            print(-arr[0])
            heapq.heappop(arr)

    else:
        heapq.heappush(arr, -now)

