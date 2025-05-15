#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9012                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9012                           #+#        #+#      #+#     #
#    Solved: 2025/05/15 10:04:05 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

# 주어진 입력받기
num_testcase = int(input())
for _ in range(num_testcase):
    parenthesis = sys.stdin.readline().rstrip()
    # VPS 검증 초기화
    is_vps = True

    # 스택 초기화
    stack = []

    for p in parenthesis:
        # "("일 경우, 스택에 추가
        if p == "(":
            stack.append(p)
            continue

        # ")"일 경우
        else:
            # 스택이 비었으면 VPS 아님
            if not stack:
                is_vps = False
                break
            # 스택이 있으면 마지막 스택이 "("인 경우임
            stack.pop()
            
    print("YES" if is_vps and not stack else "NO")