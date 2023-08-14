import heapq
import sys
#테스트케이스 수
t = int(sys.stdin.readline())
arrheap = []
heapq.heapify(arrheap)
for _ in range(t):
    k = int(sys.stdin.readline())    #연산 수

    for _ in range(k):
        now = list(map(str, sys.stdin.readline().split()))

        if now[0] == 'I':
            heapq.heappush(arrheap, int(now[1].strip()))

        elif now[0] == 'D':
            #최댓값 삭제
            if now[1] == '1':
                if len(arrheap) == 0:
                    continue
                else:
                    arrheap.pop()

            #최솟값 삭제
            elif now[1] == '-1':
                if len(arrheap) == 0:
                    continue
                else:
                    heapq.heappop(arrheap)

    if not arrheap:
        print('EMPTY')
    else:
        print(arrheap[-1], arrheap[0])


#--------------------------------------------------------------

#정답 코드
import sys
import heapq


def isEmpty(nums):
    for item in nums:
        if item[1] > 0:
            return False
    return True


t = int(sys.stdin.readline())

for i in range(t):
    min_heap = []
    max_heap = []
    nums = dict()
    k = int(sys.stdin.readline())

    for j in range(k):
        oprt, oprd = sys.stdin.readline().split()
        num = int(oprd)

        if oprt == 'I':
            # 중복 삽입일 때
            if num in nums:
                nums[num] += 1
            # 처음 삽입일 때
            else:
                nums[num] = 1
                # min_heap에 추가
                heapq.heappush(min_heap, num)
                # max_heap에 추가
                heapq.heappush(max_heap, -num)

        elif oprt == 'D':
            # 큐가 비어있지 않을 때만
            if not isEmpty(nums.items()):
                # 최댓값을 제거
                if num == 1:
                    while -max_heap[0] not in nums or nums[-max_heap[0]] < 1:
                        temp = -heapq.heappop(max_heap)
                        if temp in nums:
                            del (nums[temp])
                    nums[-max_heap[0]] -= 1
                # 최솟값을 제거
                else:
                    while min_heap[0] not in nums or nums[min_heap[0]] < 1:
                        temp = heapq.heappop(min_heap)
                        if temp in nums:
                            del (nums[temp])
                    nums[min_heap[0]] -= 1

    # 결과 출력
    if isEmpty(nums.items()):
        print('EMPTY')
    else:
        while min_heap[0] not in nums or nums[min_heap[0]] < 1:
            heapq.heappop(min_heap)
        while -max_heap[0] not in nums or nums[-max_heap[0]] < 1:
            heapq.heappop(max_heap)
        print(-max_heap[0], min_heap[0])