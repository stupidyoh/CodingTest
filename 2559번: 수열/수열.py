#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2559                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2559                           #+#        #+#      #+#     #
#    Solved: 2025/05/29 10:02:17 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# v2
# 처음으로 구간합이 생기는 지점까지는 생략

# 주어진 입력받기
days, window_length = map(int, input().split())
temperatures = list(map(int, input().split()))

# 첫 구간합 계산
init_sum = sum(temperatures[:window_length])

# 최대 구간합 초기화
max_sum = init_sum

# 첫 구간합 이후 구간만 계산
for t in range(days-window_length):
    init_sum += temperatures[window_length+t] - temperatures[t]

    if init_sum > max_sum:
        max_sum = init_sum

print(max_sum)

#  **************************************************************************  #

# v1
# 요소 하나씩 탐색하며 구간합 => 시간 초과

# from collections import deque

# days, window_length = map(int, input().split())
# temperatures = list(map(int, input().split()))

# q = deque([])
# max_sum = -float('inf')

# for temperature in temperatures:
#     q.append(temperature)

#     if len(q) < window_length:
#         continue

#     if len(q) > window_length:
#         q.popleft()

#     if sum(q) > max_sum:
#         max_sum = sum(q)

# print(max_sum)


    