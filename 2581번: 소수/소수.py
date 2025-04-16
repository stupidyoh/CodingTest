#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2581                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2581                           #+#        #+#      #+#     #
#    Solved: 2025/04/16 09:30:56 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# v2
# 에라토스테네스의 체 활용하여 소수 찾기 구현

m = int(input())
n = int(input())

# 에라토스테네스의 체
is_prime = [i for i in range(n+1)]
is_prime[0] = 0
is_prime[1] = 0

for i in range(2, int(n**0.5)+1):
    if is_prime[i] != 0:
        for j in range(2*i, n+1, i):
            is_prime[j] = 0

primes = [x for x in is_prime[m:n+1] if x != 0]
if primes:
    print(sum(primes))
    print(min(primes))
else:
    print(-1)


# ---------------------------------------------------------------------------- #

# v1
# 소수찾기 간단한 함수로 구현

# m = int(input())
# n = int(input())

# def is_prime(num):
#     if num < 2:
#         return False
    
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# prime_list = []

# for i in range(m, n+1):
#     if is_prime(i):
#         prime_list.append(i)

# if prime_list:
#     print(sum(prime_list))
#     print(min(prime_list))
# else:
#     print(-1)