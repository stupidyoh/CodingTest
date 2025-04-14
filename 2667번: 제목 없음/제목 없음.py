#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2667                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2667                           #+#        #+#      #+#     #
#    Solved: 2025/04/10 09:43:56 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n = int(input())

building_map = []
for _ in range(n):
    building_map.append(list(map(int, input().split())))

visited = [[0 for _ in range(n)] for _ in range(n)]
answer = []

for h in range(n):
    for v in range(n)