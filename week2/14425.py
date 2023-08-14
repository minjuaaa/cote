import sys

n, m = map(int, sys.stdin.readline().split())
# sys시간줄이기

s = set()
#set으로 시간줄이기
count = 0

for _ in range(n):
    s.add(sys.stdin.readline())

for i in range(m):
    i = sys.stdin.readline()
#입력받은문자로 리스트 새로 안만들고 바로바로 확인

    if i in s:
        count+=1

print(count)
