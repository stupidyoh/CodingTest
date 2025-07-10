#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5639                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5639                           #+#        #+#      #+#     #
#    Solved: 2025/07/10 18:43:37 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

# 재귀 한도 늘림
sys.setrecursionlimit(10**9)

# 주어진 입력받기
tree = []
while True:
    try:
        tree.append(int(sys.stdin.readline()))
    except:
        break

# 후위 순회
def postorder_traversal(tlist):
    # 빈 리스트인 경우
    if len(tlist) == 0:
        return 
    
    # 맨 처음 수를 root(mid)
    mid = tlist[0]
    left = tlist[1:] # 전부 root보다 작을 경우
    right = []
    for i in range(1, len(tlist)):
        # root 보다 큰 수가 있을 경우
        if tlist[i] > mid:
            left = tlist[1:i]
            right = tlist[i:]
            break
    
    # 재귀적으로 좌측(작은쪽)부터 순회
    postorder_traversal(left)
    postorder_traversal(right)
    print(mid) # 재귀가 끝날 때 출력(후위 순회 출력)
        
postorder_traversal(tree)
