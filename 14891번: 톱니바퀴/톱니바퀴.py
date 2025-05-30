#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14891                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14891                          #+#        #+#      #+#     #
#    Solved: 2025/05/30 11:15:50 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 맞닿은 부분의 인덱스
# n번의 2 - n+1번의 6

import sys

# 주어진 입력받기
wheel1 = input()
wheel2 = input()
wheel3 = input()
wheel4 = input()
wheels = [wheel1, wheel2, wheel3, wheel4]
num_rotate = int(input())
for _ in range(num_rotate):
    target_wheel, is_clockwise = map(int, sys.stdin.readline().split())
    
    # 회전 여부 판별
    rotations = [0, 0, 0, 0]
    rotations[target_wheel-1] = is_clockwise

    # 왼쪽 톱니바퀴 회전 여부 판별
    for i in range(target_wheel-1, -1, -1):
        if i == 0:
            break
        if wheels[i-1][2] != wheels[i][6]:
            rotations[i-1] = -rotations[i]
        else:
            break
    
    # 오른쪽 톱니바퀴 회전 여부 판별
    for i in range(target_wheel-1, 3):
        if wheels[i][2] != wheels[i+1][6]:
            rotations[i+1] = -rotations[i]
        else:
            break

    # 회전 구현
    for i in range(4):
        if rotations[i] == 1:
            wheels[i] = wheels[i][-1] + wheels[i][:-1]
        elif rotations[i] == -1:
            wheels[i] = wheels[i][1:] + wheels[i][0]
    # print(rotations)
    # print(wheels)

# 점수합 계산
sum_score = sum(int(wheels[i][0]) * 2**i for i in range(4))
print(sum_score)