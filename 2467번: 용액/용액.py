#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2467                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2467                           #+#        #+#      #+#     #
#    Solved: 2025/07/15 17:25:59 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 주어진 입력받기
N = int(input())
solutions = list(map(int, input().split()))

# 투 포인터 초기화
left = 0
right = N - 1

# 정답 초기화
min_sum = abs(solutions[left] + solutions[right])
sol_1_idx = left
sol_2_idx = right

# 이분탐색
while left < right:
    sum_sol = solutions[left] + solutions[right]

    # 두 수의 합이 0에 더 가깝다면 정답 갱신
    if abs(sum_sol) < min_sum:
        min_sum = abs(sum_sol)
        sol_1_idx = left
        sol_2_idx = right

        # 두 수의 합이 0이라면 탐색 중단
        if min_sum == 0:
            break

    # 합이 음수면 좌측 포인터 증가
    if sum_sol < 0:
        left += 1
    # 합이 양수면 우측 포인터 증가
    else:
        right -= 1

# 두 용액 특성값 출력
print(solutions[sol_1_idx], solutions[sol_2_idx])