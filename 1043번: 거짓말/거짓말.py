#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1043                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1043                           #+#        #+#      #+#     #
#    Solved: 2025/06/26 18:36:43 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 주어진 입력받기
num_people, num_party = map(int, input().split())

# 분리집합 초기화(0번은 가상노드)
parents = [i for i in range(num_people+1)]

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])  # 경로 압축
    return parents[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        parents[root_y] = root_x

# 진실을 아는 사람들 입력받기
know_truth_peopel = list(map(int, input().split()))

# 진실을 아는 사람이 없으면 모든 파티에서 과장 가능
if know_truth_peopel[0] == 0:
    print(num_party)
else:
    # 진실을 아는 사람들은 0번(가상노드에 연결)
    for k in know_truth_peopel[1:]:
        union(0, k)

    parties = []
    for _ in range(num_party):
        party_info = list(map(int, input().split()))
        party_people = party_info[1:]
        parties.append(party_people)

        for i in range(1, len(party_people)):
            union(party_people[0], party_people[i])

    count = 0
    for party in parties:
        if find(party[0]) != find(0):
            count += 1

    print(count)