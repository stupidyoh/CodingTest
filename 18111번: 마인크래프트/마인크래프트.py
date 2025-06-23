#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 18111                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/18111                          #+#        #+#      #+#     #
#    Solved: 2025/06/23 18:52:39 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


import sys

# 주어진 입력받기
n, m, b = map(int, input().split())
heights_map = []
for _ in range(n):
    heights_map.append(list(map(int, sys.stdin.readline().split())))

answer = sys.maxsize
heights = {}
max_height = 0
min_height = 256

for i in range(n):
    for j in range(m):
        height = heights_map[i][j]
        if height > max_height:
            max_height = height
        if height < min_height:
            min_height = height
        heights[height] = heights.get(height, 0) + 1

for h in range(min_height, max_height+1):
    # 필요한 블록 갯수 계산
    block_needed = 0
    block_have = 0
    # 소요시간 계산
    time_taken = 0

    for gh, c in heights.items():
        # 땅의 높이가 목표 높이보다 높으면
        if gh > h:
            # 블록 제거 후 인벤토리에 넣기
            block_have += (gh - h) * c
        # 땅의 높이가 목표 높이보다 낮으면
        else:
            # 차이만큼 블록을 채우기
            block_needed += (h - gh) * c

    # 필요한 블록이 가진 블록보다 많으면 계산 x
    if block_needed > block_have + b:
        continue

    # 소요 시간 계산
    time_taken = 2 * block_have + block_needed

    # 필요한 블록이 가진 블록보다 적을 때 소요시간과 목표 높이 저장
    if time_taken <= answer:
        answer = time_taken
        ground_level = h

# 정답 출력
print(answer, ground_level)