#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2309                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2309                           #+#        #+#      #+#     #
#    Solved: 2025/04/08 09:30:33 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from itertools import combinations

heights = [int(input()) for _ in range(9)]
for comb in combinations(heights, 7):
    if sum(comb) == 100:
        for item in sorted(comb):
            print(item)
            
        break