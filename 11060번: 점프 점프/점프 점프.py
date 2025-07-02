#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11060                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11060                          #+#        #+#      #+#     #
#    Solved: 2025/07/02 20:06:22 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 주어진 입력받기
N = int(input())
jumps = list(map(int, input().split()))

# dp 정의
dp = [1000] * N
dp[0] = 0

# dp 계산
# bottom-up
# dp[i] = i번째에 도달하는데 필요한 최소 점프
for i in range(N):
    for j in range(i+1, i+jumps[i]+1):
        if j < N:
            dp[j] = min(dp[j], dp[i] + 1)

# 오른쪽 끝 칸 도달에 필요한 최소 점프 수 출력
if dp[N-1] == 1000:
    print(-1)
else:
    print(dp[N-1])