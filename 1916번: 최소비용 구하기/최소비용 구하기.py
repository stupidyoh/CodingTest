#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1916                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1916                           #+#        #+#      #+#     #
#    Solved: 2025/05/07 09:26:12 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


import sys
from heapq import heappop, heappush

# 주어진 입력받기
num_city = int(input())
num_bus = int(input())
bus_infos = [[] for _ in range(num_city+1)]
for _ in range(num_bus):
    d, a, c = map(int, sys.stdin.readline().split())
    bus_infos[d].append((a, c))
start, end = map(int, input().split())

# 비용 계산
cost_infos = [float('inf') for _ in range(num_city+1)]

# 다익스트라 알고리즘
def dijkstra(s):
    visited = [False for _ in range(num_city+1)]
    cost_infos[s] = 0
    q = [(0, s)]

    while q:
        cost, depart = heappop(q)

        if visited[depart]:
            continue

        visited[depart] = True

        for arrive, new_cost in bus_infos[depart]:
            total_cost = cost + new_cost
            if total_cost < cost_infos[arrive]:
                cost_infos[arrive] = total_cost
                heappush(q, (total_cost, arrive))

dijkstra(start)
print(cost_infos[end])
