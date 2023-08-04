from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())
arr = deque()
num = []

for _ in range(N):
    num.clear()
    num = sys.stdin.readline().rstrip().split()
    if num[0] == 'push':
        arr.append(int(num[1]))

    elif num[0] == 'pop':
        if len(arr)==0:
            print(-1)
        else:
            print(arr[0])
            arr.popleft()

    elif num[0] == 'size':
        print(len(arr))

    elif num[0] == 'empty':
        if len(arr)==0:
            print(1)
        else:
            print(0)

    elif num[0] == 'front':
        if len(arr) != 0:
            print(arr[0])
        elif len(arr) == 0:
            print(-1)

    elif num[0] == 'back':
        if len(arr) != 0:
            print(arr[len(arr)-1])
        elif len(arr) == 0:
            print(-1)
