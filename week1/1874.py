n = int(input())

stack = []
arr = []
now = 1

for _ in range(n):
    num = int(input())


    while now <= num:
        arr.append('+')
        stack.append(now)
        now += 1

    if stack[-1] == num:
        stack.pop()
        arr.append('-')
    else:
        arr.clear()
        arr.append('NO')
        break

for i in arr:
    print(i)