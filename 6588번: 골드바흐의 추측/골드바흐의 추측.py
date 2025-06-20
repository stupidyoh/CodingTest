#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 6588                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/6588                           #+#        #+#      #+#     #
#    Solved: 2025/06/20 18:46:28 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

# 에라토스테네스의 체
max_limit = 1000001

is_prime = [True] * max_limit
is_prime[0] = False
is_prime[1] = False

for i in range(2, int(max_limit**0.5)+1):
    if is_prime[i]:
        for j in range(2*i, max_limit, i):
            is_prime[j] = False

# 테스트케이스 반복
while True:
    
    # 주어진 입력받기
    n = int(sys.stdin.readline())
    is_goldbach = False

    # 테스트케이스 종료
    if n == 0:
        break

    # 첫 소수부터 테스트 정수의 절반까지 홀수들에 대해서만 진행
    for a in range(3, n//2 + 1, 2):
        # a, b 모두 소수이면
        if is_prime[a] and is_prime[n-a]:
            print(f"{n} = {a} + {n-a}")
            is_goldbach = True
            break
    
    # 두 소수의 합으로 이뤄지지 않았다면
    if not is_goldbach:
        print("Goldbach's conjecture is wrong.")