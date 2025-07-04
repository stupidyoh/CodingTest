#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 20040                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/20040                          #+#        #+#      #+#     #
#    Solved: 2025/07/04 18:49:46 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

# 주어진 입력받기
num_point, num_turn = map(int, sys.stdin.readline().split())

is_cycle = False
parents = [i for i in range(num_point)]

def find(n):
    if n != parents[n]:
        parents[n] = find(parents[n])
    return parents[n]

def union(a, b):
    a = find(a)
    b = find(b)
    # 작은 쪽이 부모 노드가 되도록
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

# 각 차례마다 사이클 여부 판단
for nt in range(num_turn):
    n1, n2 = map(int, sys.stdin.readline().split())

    # 두 노드의 부모가 같으면 사이클
    if find(n1) == find(n2):
        is_cycle = True
        turn = nt + 1
        break

    union(n1, n2)
    # print(parents)

# 게임 종료 차례 출력
if is_cycle:
    print(turn)
else:
    print(0)