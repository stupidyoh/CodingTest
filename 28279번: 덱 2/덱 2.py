#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 28279                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/28279                          #+#        #+#      #+#     #
#    Solved: 2025/05/02 09:35:40 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque
import sys

# 주어진 입력 받기
n = int(input())

q = deque([])
for _ in range(n):
    command = list(map(int, sys.stdin.readline().split()))

    if command[0] == 1:
        q.append(command[1])
    elif command[0] == 2:
        q.appendleft(command[1])
    elif command[0] == 3:
        print(q.pop() if q else -1)
    elif command[0] == 4:
        print(q.popleft() if q else -1)
    elif command[0] == 5:
        print(len(q))
    elif command[0] == 6:
        print(1 if not q else 0)
    elif command[0] == 7:
        print(q[-1] if q else -1)
    elif command[0] == 8:
        print(q[0] if q else -1)