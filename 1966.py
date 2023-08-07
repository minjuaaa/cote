from collections import deque

tc = int(input())
for _ in range(tc):
    # 문서갯수m, 궁금문서n
    n, m = map(int, input().split())
    pri = list(map(int, input().split()))
    count = 0

    q = deque([(val, idx) for idx, val in enumerate(pri)])  # (값, 인덱스)의 튜플을 큐에 저장

    while q:
        val, idx = q.popleft() # 맨 앞 확인

        if val == max(pri):  # 가장 큰 중요도라면 출력진행
            count += 1
            if idx == m:  # 궁금문서라면 반복 종료
                break
            pri[idx] = 0  # 출력한 문서는 중요도 0으로 변경

        else:   # 가장중요 X면
            q.append((val, idx))  # 큐의 맨 뒤로 다시 붙임

    print(count)
