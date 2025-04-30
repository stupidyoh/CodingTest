#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 4949                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/4949                           #+#        #+#      #+#     #
#    Solved: 2025/04/30 09:31:35 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

while True:
    sentence = sys.stdin.readline()
    # print(sentence)

    if sentence[0] == ".":
        break

    stack = []
    is_balance = True
    for s in sentence:
        if s == ".":
            break

        if s == "(" or s == "[":
            stack.append(s)
        elif s == ")":
            if not stack or stack.pop() != "(":
                is_balance = False
                break
        elif s == "]":
            if not stack or stack.pop() != "[":
                is_balance = False
                break

    if stack or not is_balance:
        print("no")
    else:
        print("yes")
