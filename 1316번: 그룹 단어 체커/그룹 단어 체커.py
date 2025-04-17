#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1316                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1316                           #+#        #+#      #+#     #
#    Solved: 2025/04/17 09:31:43 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# v2
# 연속 중복 문자를 제거한 후 set을 사용하여 길이 비교

n = int(input())
result = 0

for _ in range(n):
    word = input()
    compressed = word[0]

    for i in range(1, len(word)):
        if word[i] != compressed[-1]:
            compressed += word[i]

    if len(compressed) == len(set(compressed)):
        result += 1

print(result)

# --------------------------------------------------------------------------- # 

# v1
# 순차적으로 돌면서 현재 문자가 이전 문자와 다른데 사용된 적이 있다면 검출

# n = int(input())
# result = 0

# for _ in range(n):
#     word = str(input())
#     used = set()
#     is_not_used = True

#     prev = word[0]
#     used.add(prev)

#     for i in range(1, len(word)):
#         cur = word[i]

#         if prev != cur and cur in used:
#             is_not_used = False
#             break

#         used.add(cur)
#         prev = cur

#     if is_not_used:
#         result += 1

# print(result)

    
