#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1978                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1978                           #+#        #+#      #+#     #
#    Solved: 2025/04/14 09:32:08 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n = int(input())
given_nums = list(map(int, input().split()))
result = 0

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


for given_num in given_nums:
    if is_prime(given_num):
        result += 1
    
print(result)