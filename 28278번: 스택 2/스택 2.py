#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 28278                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/28278                          #+#        #+#      #+#     #
#    Solved: 2025/04/28 09:33:18 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# v2
# 코드 간결화

import sys

n = int(input())
stack = []

for _ in range(n):
    command = sys.stdin.readline().split()
    op = int(command[0])

    if op == 1:
        stack.append(int(command[1]))
    elif op == 2:
        print(stack.pop() if stack else -1)
    elif op == 3:
        print(len(stack))
    elif op == 4:
        print(1 if not stack else 0)
    elif op == 5:
        print(stack[-1] if stack else -1)


#  **************************************************************************  #

# v1
# 직관적 풀이

# import sys

# # 주어진 입력받기
# n = int(input())

# # 스택 정의
# stack = []

# # 명령 수행
# for _ in range(n):
#     command = list(map(int, sys.stdin.readline().split()))

#     if command[0] == 1:
#         stack.append(command[-1])

#     elif command[0] == 2:
#         if stack:
#             print(stack.pop())
#         else:
#             print(-1)
    
#     elif command[0] == 3:
#         print(len(stack))

#     elif command[0] == 4:
#         if not stack:
#             print(1)
#         else:
#             print(0)

#     elif command[0] == 5:
#         if stack:
#             print(stack[-1])
#         else:
#             print(-1)