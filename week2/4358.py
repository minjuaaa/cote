import sys

n = 'a'
dic = {}
count = 0

while 1:
    n = sys.stdin.readline().strip()  # 줄바꿈 문자 제거.strip()

    if n == '':
        break

    count += 1
    if n not in dic:
        dic[n] = 1

    elif n in dic:
        dic[n] += 1


#key를 기준으로 정렬
for key, value in sorted(dic.items()):
    num = (value/count)*100
    print(key, "%0.4f"%num)

# round(실수, 표기할 자리수) 이건 반올림이라 쓰면 안됨!!!!!
