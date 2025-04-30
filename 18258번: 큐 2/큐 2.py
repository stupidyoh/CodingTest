#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 18258                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/18258                          #+#        #+#      #+#     #
#    Solved: 2025/04/29 11:35:15 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# v1
# deque 사용

import sys
from collections import deque

# 주어진 입력받기
n = int(input())

q = deque()
for _ in range(n):
    command = sys.stdin.readline().split()
    
    if command[0] == "push":
        q.appendleft(int(command[1]))
    elif command[0] == "pop":
        print(q.pop() if q else -1)
    elif command[0] == "size":
        print(len(q))
    elif command[0] == "empty":
        print(1 if not q else 0)
    elif command[0] == "front":
        print(q[-1] if q else -1)
    elif command[0] == "back":
        print(q[0] if q else -1)