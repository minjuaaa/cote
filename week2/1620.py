n, m = map(int, input().split())
dic = {}

for i in range(1, n+1):
    dic[i] = input()

revdic = {v:k for k,v in dic.items()}
#처음에는 딕셔너리 하나 더 안만들고 그냥 값으로 키를 찾았는데 시간초과 나옴... 이게 더 빠르다...!

for j in range(m):
    now = input()
    if now.isdecimal() == 1:
        print(dic[int(now)])
    else:
        print(revdic[now])

