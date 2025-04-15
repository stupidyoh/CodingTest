#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1292                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1292                           #+#        #+#      #+#     #
#    Solved: 2025/04/15 09:31:04 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# v3
# 수열을 만들어서 직접 구하기

start, end = map(int, input().split())

sequence = []
for i in range(1, end + 1):
    sequence.extend([i] * i)

print(sum(sequence[start-1:end]))


# --------------------------------------------------------------------------- #

# v2
# 순차적으로 start부터 end까지의 합

# start, end = map(int, input().split())

# result = 0 
# num = 1
# count = 0

# for i in range(1, end + 1):
#     if count == num:
#         num += 1
#         count = 0
#     count += 1

#     if i >= start:
#         result += num

# print(result)

# --------------------------------------------------------------------------- #

# v1
# end까지의 합 - (start-1)까지의 합

# start, end = map(int, input().split())

# def sum_n(n):
#     result = 0
#     cur_num = 1
#     count = 0
#     for _ in range(1, n + 1):
#         count += 1
#         result += cur_num
#         if count == cur_num:
#             cur_num +=1
#             count = 0
#     return result

# print(sum_n(end) - sum_n(start-1))