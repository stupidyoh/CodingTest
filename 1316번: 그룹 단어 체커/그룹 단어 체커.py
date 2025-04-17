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
n = int(input())
result = 0

for _ in range(n):
    word = str(input())
    used = set()
    is_not_used = True

    prev = word[0]
    used.add(prev)

    for i in range(1, len(word)):
        cur = word[i]

        if prev != cur and cur in used:
            is_not_used = False
            break

        used.add(cur)
        prev = cur

    if is_not_used:
        result += 1

print(result)

    
