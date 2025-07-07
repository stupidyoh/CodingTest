#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 19637                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/19637                          #+#        #+#      #+#     #
#    Solved: 2025/07/07 18:57:22 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from bisect import bisect_left

# 주어진 입력받기
num_title, num_person = map(int, sys.stdin.readline().split())

# 칭호, 전투력 상한값 별도 리스트로 초기화
titles = [] 
powers = []
for _ in range(num_title):
    t, p = map(str, sys.stdin.readline().split())
    p = int(p)
    titles.append(t)
    powers.append(p)

# 캐릭터의 전투력에 따른 입력/계산
for _ in range(num_person):
    power = int(sys.stdin.readline().rstrip())
    
    # 이분탐색으로 최대 상한선의 인덱스 구하기
    idx = bisect_left(powers, power)

    # 해당 인덱스를 칭호 인덱스로 출력
    print(titles[idx])