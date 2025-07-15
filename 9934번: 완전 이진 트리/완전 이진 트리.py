#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9934                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9934                           #+#        #+#      #+#     #
#    Solved: 2025/07/15 17:25:54 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 주어진 입력받기
K = int(input())
buildings = list(map(int, input().split()))

# 정답 초기화
tree = [[] for _ in range(K)]

# tree 채우기(중위 순회)
def inorder_traversal(building_list, depth):
    # 리스트의 가운데 값을 정답 리스트에 추가
    mid = len(building_list) // 2
    tree[depth].append(building_list[mid])

    # 깊이가 트리 높이와 같으면 return
    if depth == K-1:
        return
    
    # 중앙 기준 좌측 리스트에 대해서 재귀
    left = building_list[:mid]
    inorder_traversal(left, depth+1)

    # 중앙 기준 우측 리스트에 대해서 재귀
    right = building_list[mid+1:]
    inorder_traversal(right, depth+1)

# 중위 순회
inorder_traversal(buildings, 0)

# 정답 출력
for t in tree:
    print(*t)