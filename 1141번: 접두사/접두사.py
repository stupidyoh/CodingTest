#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1141                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1141                           #+#        #+#      #+#     #
#    Solved: 2025/04/29 09:31:36 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# v2
# 최적화

import sys

n = int(input())
words = [sys.stdin.readline().strip() for _ in range(n)]

# 중복 제거
words = list(set(words))

# 길이 기준 정렬 (긴 단어 우선)
words.sort(reverse=True)

# 접두사 체크 함수
def is_not_prefix_of_any(word, selected):
    for s in selected:
        if s.startswith(word):
            return False
    return True

selected = []
for word in words:
    if is_not_prefix_of_any(word, selected):
        selected.append(word)

print(len(selected))

#  **************************************************************************  #

# v1
# 새로운 요소가 기존 요소를 접두사로 포함하고 있으면 기존 요소를 삭제

# # 주어진 입력받기
# n = int(input())

# words = []
# for _ in range(n):
#     words.append(input())
# # 사전식 정렬을 통한 접두사 파악 용이
# words.sort()
# # print(words)

# stack = []
# for word in words:
#     # 아무것도 없을시 스택에 추가
#     if not stack:
#         stack.append(word)
#         # print("stack: ", stack)
#         continue

#     # 스택에 있는 요소들과 비교
#     for s in stack:
#         # 스택 요소가 새로운 요소보다 길이가 짧고 새로운 요소의 접두사인 경우 삭제
#         if len(s) <= len(word) and word.startswith(s):
#             stack.remove(s)
#             # print("stack: ", stack)
#             continue
#     # 새로운 요소를 스택에 추가
#     stack.append(word)
#     # print("stack: ", stack)

# print(len(stack))