#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2164                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2164                           #+#        #+#      #+#     #
#    Solved: 2025/05/01 09:29:51 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque

# 주어진 입력받기
n = int(input())

q = deque([i for i in range(1, n+1)])

while len(q) > 1:
    q.popleft()
    # print(q)
    q.append(q.popleft())
    # print(q)

print(q[0])