#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 13023                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/13023                          #+#        #+#      #+#     #
#    Solved: 2025/06/24 19:59:52 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

# 주어진 입력받기
N, M = map(int, input().split())
# 그래프 만들기
relations = dict()
for i in range(N):
    relations[i] = []
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    relations[a].append(b)
    relations[b].append(a)

# 조건에 맞는 친구 관계 초기화
is_exist = False

# 방문여부 확인
visited = [False] * N

# 조건 탐색
def dfs(start, depth):
    # 조건 만족시 처리
    if depth == 4:
        global is_exist
        is_exist = True
        return
    
    # 현재 노드 방문 처리
    visited[start] = True

    # 친구 관계가 있으면 재귀 탐색
    for next in relations[start]:
        # 방문 여부 확인하여 순환 방지
        if not visited[next]:
            dfs(next, depth+1)
    # 방문 여부 해제
    visited[start] = False

# 모든 사람들에 대해 dfs 탐색
for i in range(N):
    # 답 찾았으면 종료
    if is_exist:
        break
    dfs(i, 0)

# 있으면 1 없으면 0 출력
print(1 if is_exist else 0)