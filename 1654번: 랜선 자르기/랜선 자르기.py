#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1654                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1654                           #+#        #+#      #+#     #
#    Solved: 2025/06/28 18:00:40 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

# 주어진 입력 받기
lan_reserved, lan_need = map(int, input().split())
lengths = [int(sys.stdin.readline()) for _ in range(lan_reserved)]

# 이분탐색 
left, right = 1, max(lengths)
while left <= right:
    mid = (left + right) // 2
    # 만들 수 있는 랜선 갯수 계산
    num_lan = 0
    for length in lengths:
        num_lan += length // mid

    if num_lan >= lan_need:
        left = mid + 1
    else:
        right = mid - 1

print(right)