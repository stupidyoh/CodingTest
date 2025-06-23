#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 13904                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/13904                          #+#        #+#      #+#     #
#    Solved: 2025/06/23 18:52:26 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
import heapq

# 힙큐 초기화
hq = []
# 최대 마감일 초기화
max_deadline= 0

# 주어진 입력받기
N = int(input())
for _ in range(N):
    d, w = map(int, sys.stdin.readline().split())
    # 힙큐 삽입
    heapq.heappush(hq, (-w, d)) # 점수가 높은 순으로 정렬하기 위해 - 붙임
    # 최대 마감일 계산
    if max_deadline < d:
        max_deadline = d

# 할당 여부 리스트 초기화
assigned = [False] * (max_deadline + 1)
# 최대 점수값 초기화
max_score = 0

while hq:
    w, d = heapq.heappop(hq)
    w = -w

    # 마감일부터 역순으로 해당 날짜에 과제가 할당되었는지 확인
    for i in range(d, 0, -1):
        # 할당되어있으면 그 다음날 탐색
        if assigned[i]:
            continue
        # 할당 없으면 할당 및 최대점수 갱신
        assigned[i] = True
        max_score += w
        break
# 정답 출력
print(max_score)