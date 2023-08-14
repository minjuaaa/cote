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
            #진짜값만 출력
            print(arr[0][1])
            heapq.heappop(arr)

    else:
        heapq.heappush(arr, (abs(now),now))
        # 튜플로 힙 추가하는 방법
        # 정렬은 첫번째 기준으로 됨 (절댓값, 진짜값)
