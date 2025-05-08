#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10815                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10815                          #+#        #+#      #+#     #
#    Solved: 2025/05/08 09:09:06 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# v2
# 집합 활용

import sys

# 주어진 입력받기
num_card = int(input())
cards = set(map(int, sys.stdin.readline().split()))
num_target = int(input())
targets = list(map(int, sys.stdin.readline().split()))

for target in targets:
    if target in cards:
        print(1, end=' ')
    else:
        print(0, end=' ')


#  **************************************************************************  #

# v1
# 이분탐색 

# import sys

# # 주어진 입력받기
# num_card = int(input())
# cards = list(map(int, sys.stdin.readline().split()))
# num_target = int(input())
# targets = list(map(int, sys.stdin.readline().split()))

# # 이분탐색을 위한 정렬
# cards.sort()

# # 각 정수별 숫자카드가 있는지 확인
# for target in targets:
#     left, right = 0, num_card - 1
#     is_target = 0

#     # 이분탐색 알고리즘
#     while left <= right:
#         mid = (left + right) // 2
#         if cards[mid] == target:
#             is_target = 1
#             break
#         elif cards[mid] > target:
#             right = mid-1
#         elif cards[mid] < target:
#             left = mid+1
#     print(is_target, end=' ')