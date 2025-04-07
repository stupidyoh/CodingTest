#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2460                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2460                           #+#        #+#      #+#     #
#    Solved: 2025/04/04 17:29:23 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
current_num = 0
max_num = 0

for _ in range(10):
    people_out, people_in = map(int, input().split())
    
    current_num -= people_out   
    current_num = min(10000, current_num + people_in)
        
    max_num = max(max_num, current_num)
        
print(max_num)