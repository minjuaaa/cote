from collections import deque

answer =[]
n, k = map(int, input().split())

q = deque([i for i in range(1, n+1)])

while len(answer) < n:
    for i in range(k):
        if i == k-1:
            answer.append(q.popleft())
        else:
            q.append(q.popleft())

print("<", ', '.join(str(i) for i in answer), ">", sep="") 
#출력주의!!!
