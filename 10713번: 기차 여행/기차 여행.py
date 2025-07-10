#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10713                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10713                          #+#        #+#      #+#     #
#    Solved: 2025/07/09 20:33:51 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
input = sys.stdin.readline

# 주어진 입력받기
num_city, num_visit = map(int, input().split())
cities = list(map(int, input().split()))
prices = [list(map(int, input().split())) for _ in range(num_city-1)]

# 차분 배열을 통해 열차 이용 횟수 계산
diff = [0] * (num_city)
for i in range(num_visit-1):
    start_train = min(cities[i],cities[i+1])
    end_train = max(cities[i],cities[i+1])
    diff[start_train-1] += 1
    diff[end_train-1] -= 1
count_train = [0] * (num_city - 1)
count_train[0] = diff[0]
for i in range(1, num_city-1):
    count_train[i] = count_train[i-1] + diff[i]

# 최소 이용금액 계산
total_fee = 0
for ct in range(num_city-1):
    if count_train[ct] == 0:
        continue

    # 티켓 가격
    price_ticket = count_train[ct] * prices[ct][0]
    # IC카드 가격
    price_card = count_train[ct] * prices[ct][1] + prices[ct][2]
    
    # 티켓이 더 싼 경우
    if price_ticket <= price_card:
        total_fee += price_ticket
    # IC카드가 더 싼 경우
    else:
        total_fee += price_card

print(total_fee)
