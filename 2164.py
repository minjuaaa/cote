from collections import deque
n = int(input())
count = 0
arr = deque()

for j in range(n):
    arr.append(int(j+1))


while(len(arr) != 1):
    count = count + 1
    if count%2 == 1:
        arr.popleft()

    elif count%2 == 0:
        arr.append(arr[0])
        arr.popleft()

print(arr[0])

