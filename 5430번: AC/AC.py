#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5430                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5430                           #+#        #+#      #+#     #
#    Solved: 2025/06/24 19:59:39 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    integers = input()[1:-1].split(",")
    integers = deque(integers)

    if n == 0:
        integers = []

    is_error = False
    is_flipped = -1

    for func in p:
        if func == "R":
            is_flipped = -is_flipped
        elif func == "D":
            if len(integers) < 1:
                is_error = True
                print("error")
                break
            # 안뒤집혔으면 앞에서 제거
            elif is_flipped == -1:
                integers.popleft()
            # 뒤집혔으면 뒤에서 제거
            else:
                integers.pop()
    if not is_error:
        if is_flipped == -1:
            print("[" + ",".join(integers) + "]")
        else:
            integers.reverse()
            print("[" + ",".join(integers) + "]")

#  **************************************************************************  #

# # 주어진 입력받기
# T = int(input())
# for _ in range(T):
#     p = input()
#     n = int(input())
#     temp_integers = input()
#     if temp_integers == "[]":
#         integers = list()
#     else:
#         integers = list(map(int, temp_integers[1:-1].split(",")))


#     is_error = False
#     is_flipped = -1 # 1: 뒤집힘 / -1: 안뒤집힘

#     for func in p:
#         if func == "R":
#             is_flipped = -is_flipped
#         elif func == "D":
#             if len(integers) == 0:
#                 is_error = True
#                 break
#             # 안뒤집혔으면 앞에서 제거
#             elif is_flipped == -1:
#                 integers.pop(0)
#             # 뒤집혔으면 뒤에서 제거
#             else:
#                 integers.pop()
#     if is_error:
#         print("error")
#     elif is_flipped == -1:
#         print(str(integers).replace(" ", ""))
#     else:
#         integers.reverse()
#         print(str(integers).replace(" ", ""))