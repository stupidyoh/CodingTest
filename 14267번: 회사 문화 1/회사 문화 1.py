#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14267                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14267                          #+#        #+#      #+#     #
#    Solved: 2025/07/03 18:49:54 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# v2
# 다이나믹 프로그래밍

import sys

# 주어진 입력받기
num_employee, num_praise = map(int, sys.stdin.readline().split())
bosses = [0] + list(map(int, sys.stdin.readline().split()))
praises = [0] * (num_employee + 1)

# 초기에 본인이 받은 칭찬 점수 계산
for _ in range(num_praise):
    e, p = map(int, sys.stdin.readline().split())
    praises[e] += p

# 사장부터 차례대로 본인이 받은 칭찬을 누적해서 내려줌
for i in range(2, num_employee+1):
    praises[i] += praises[bosses[i]]

# 칭찬 정도 출력
print(*praises[1:])

#  **************************************************************************  #

# v1
# 그래프 + DFS
# 런타임 에러

# import sys

# # 주어진 입력받기
# num_employee, num_praise = map(int, sys.stdin.readline().split())

# bosses = list(map(int, sys.stdin.readline().split()))
# underling = {}
# for i in range(1, num_employee):
#     if bosses[i] not in underling:
#         underling[bosses[i]] = []

# for i in range(1, num_employee):
#     underling[bosses[i]].append(i+1)

# # 칭찬 받은 정도 초기화
# praises = [0] * num_employee

# def dfs(cur_employee, praise_point):
#     # n번째 직원이 받은 칭찬 점수
#     praises[cur_employee-1] += praise_point
#     # n번 직원의 부하
#     if cur_employee in underling:
#         for u in underling[cur_employee]:
#             dfs(u, praise_point)

# for _ in range(num_praise):
#     e, p = map(int, sys.stdin.readline().split())
#     dfs(e, p)

# # 전 직원 칭찬 받은 정도 출력
# print(*praises)