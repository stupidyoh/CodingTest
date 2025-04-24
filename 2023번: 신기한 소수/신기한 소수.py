#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2023                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2023                           #+#        #+#      #+#     #
#    Solved: 2025/04/24 10:17:16 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 주어진 입력받기
n = int(input())

# 소수 판별 함수 정의
def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
        
    return True

awesome_prime = []

# 백트래킹
def back():
    if len(awesome_prime) == n:
        print(int(''.join(map(str, awesome_prime))))
        return
    
    # 0이 붙는 경우는 소수가 아니므로 제외
    for i in range(1, 10):
        awesome_prime.append(i)
        # print(awesome_prime)
        if is_prime(int(''.join(map(str, awesome_prime)))):
            back()

        awesome_prime.pop()

back()


