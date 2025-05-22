#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 4779                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/4779                           #+#        #+#      #+#     #
#    Solved: 2025/05/22 09:58:45 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# v2
# 재귀

def cantor(n):
    if n == 0:
        return "-"
    prev = cantor(n-1)
    return prev + " " * len(prev) + prev


while True:
    try:
        n = int(input())
        print(cantor(n))

    except:
        break


#  **************************************************************************  #

# v1
# 반복문

# while True:
#     try:
#         n = int(input())
#         lines = "-"

#         for i in range(n):
#             lines = lines + (" " * len(lines)) + lines

#         print(lines)

#     except:
#         break