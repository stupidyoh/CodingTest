#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 6236                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/6236                           #+#        #+#      #+#     #
#    Solved: 2025/06/28 18:00:48 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

# 주어진 입력받기
N, M = map(int, input().split())
expenses = [int(sys.stdin.readline()) for _ in range(N)]

left, right = max(expenses), sum(expenses)

# 이분탐색
while left < right:
    mid = (left + right) // 2

    cur_money = 0 # 현재 보유 금액
    num_deposit = 0 # 인출 횟수

    # 요일별 지출마다 계산
    for expense in expenses:
        if expense > cur_money:
            num_deposit += 1
            cur_money = mid
        cur_money -= expense
        

    # 인출횟수가 계획보다 적으면 금액 줄임
    if num_deposit <= M:
        right = mid
    # 반대면 금액 늘림
    else:
        left = mid + 1

# 최소 금액 출력
print(left)
