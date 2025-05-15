#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 20916                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/20916                          #+#        #+#      #+#     #
#    Solved: 2025/05/15 11:10:23 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

# 안녕한 정수인지 판별
def is_hello(num):
    if num[:4] == "2020" and num[-4:] == "2021":
        return True
    return False

# 주어진 입력받기
num_testcase = int(input())
for _ in range(num_testcase):
    num_integer = int(input())
    integers = list(map(int, sys.stdin.readline().split()))

    num_hello = 0

    # 두 수의 합이 안녕한 정수인지
    for i, num1 in enumerate(integers):
        for num2 in integers[i+1:]:
            if is_hello(str(num1+num2)):
                num_hello += 1

    print(num_hello)