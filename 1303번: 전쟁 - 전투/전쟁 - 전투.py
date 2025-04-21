#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1303                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1303                           #+#        #+#      #+#     #
#    Solved: 2025/04/21 09:44:12 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n, m = map(int, input().split())

battlefield = []
for _ in range(n):
    battlefield.append(list(input()))

visited = [[False for _ in range(m)] for _ in range(n)]

