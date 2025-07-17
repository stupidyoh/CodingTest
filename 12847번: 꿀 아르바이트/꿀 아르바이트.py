#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 12847                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/12847                          #+#        #+#      #+#     #
#    Solved: 2025/07/17 18:52:25 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 주어진 입력받기
n, m = map(int, input().split())
wages = list(map(int, input().split()))

# 현재 구간합, 최대 구간합 초기화
temp_sum_wage = max_sum_wage = sum(wages[:m])

for i in range(m, n):
    # 슬라이딩 윈도우로 현재 구간합 계산
    temp_sum_wage = temp_sum_wage + wages[i] - wages[i-m]

    # 최대 구간합 갱신
    max_sum_wage = max(temp_sum_wage, max_sum_wage)

# 최대 이익 출력
print(max_sum_wage)

#  **************************************************************************  #

# v2
# deque 활용

# from collections import deque

# # 주어진 입력받기
# n, m = map(int, input().split())
# wages = list(map(int, input().split()))

# q = deque([])
# for i in range(m):
#     q.append(wages[i])

# max_sum_wage = 0

# for i in range(m, n):
#     q.popleft()
#     q.append(wages[i])
#     if sum(q) > max_sum_wage:
#         max_sum_wage = sum(q)

# print(max_sum_wage)
#  **************************************************************************  #

# v1
# 시간초과

# # 주어진 입력받기
# n, m = map(int, input().split())
# wages = list(map(int, input().split()))

# max_sum_wage = 0

# for i in range(n-m):
#     max_sum_wage = max(sum(wages[i:i+m]), max_sum_wage)

# print(max_sum_wage)