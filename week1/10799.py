s = input()
stack=[]
now = 0
count = 0
leng = len(s)

for i in range(leng):
    if i < leng-1:
        if s[i] == '(' and s[i+1] == ')':
            count += now
            now += 1
            continue

    if s[i] == ')':
        now -= 1

    elif s[i] == '(':
        now += 1
        count += 1

print(count)
