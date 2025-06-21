#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 20920                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/20920                          #+#        #+#      #+#     #
#    Solved: 2025/06/21 11:37:29 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

# 주어진 입력받기
n, m = map(int, input().split())
words = {}
for _ in range(n):
    # \n 개행 제거
    word = sys.stdin.readline().rstrip()

    # m 이상의 단어만 카운트
    if len(word) >= m:
        words[word] = words.get(word, 0) + 1

# 정렬 기준 수립
sort_standard = []
for k, v in words.items():
    # [단어 빈도, 단어 길이, 단어] 기록
    sort_standard.append([v, len(k), k])

# 우선순위에 따라 정렬
sort_standard.sort(key = lambda x: (-x[0], -x[1], x[2]))

# 정답 출력
for _, _, w in sort_standard:
    print(w)