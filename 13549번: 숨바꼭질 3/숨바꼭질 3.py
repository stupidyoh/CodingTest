#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 13549                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/13549                          #+#        #+#      #+#     #
#    Solved: 2025/07/02 20:06:36 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque

# 주어진 입력받기
soobin, sister = map(int, input().split())
# soobin, sister = 4, 12 # 1
# soobin, sister = 3, 12 # 0
# soobin, sister = 1, 32 # 0
# soobin, sister = 2, 14 # 1
# soobin, sister = 10000, 0 # 10000
# soobin, sister = 2, 7 # 1
# soobin, sister = 1, 17 # 1
# soobin, sister = 0, 1 # 1
# soobin, sister = 0, 3 # 2
# soobin, sister = 0, 0  # 0
# soobin, sister = 3, 22 # 1
# soobin, sister = 5, 7 # 2
# soobin, sister = 1, 100000 # 5
# soobin, sister = 1, 2 # 0

time = 0

# 수빈이 동생보다 오른쪽에 있을 때에는 걷기로만 가능
if soobin >= sister:
    time = soobin - sister
# 수빈이 동생보다 왼쪽에 있을 때에는 순간이동, 걷기
else:
    # 위치별 도달시간
    pos_time = [0] * 100001

    def bfs(start):
        q = deque([start])
        visited = [0] * 100001
        visited[soobin] = 1

        while q:
            now = q.popleft()

            if now == sister:
                return pos_time[now]

            # 좌로 걷기, 우로 걷기, 순간이동
            next_walk = [now - 1, now + 1]
            next_teleport = now * 2

            # 텔레포트가 우선순위
            # (추측) 좌로 걷기가 우로 걷기보다 더 짧은 경우일 것임
            # 좌로 걸으면 x2 했을 때 우로 걷는 것보다 상대적으로 적게 커져서 목표를 넘길 확률이 적음
            # (의심) 우로 걷고 x2 했는데 목표면 그게 더 짧을 수도 있지 않을까?
            # 그렇다고 하면 좌로 먼저 갔을 때 더 짧을리가 없음

            # 텔레포트
            if (0 <= next_teleport <= 100000) and not visited[next_teleport]:
                visited[next_teleport] = 1
                pos_time[next_teleport] = pos_time[now]
                q.appendleft(next_teleport)
            # 걷기
            for next in next_walk:
                if (0 <= next <= 100000) and not visited[next]:
                    visited[next] = 1
                    pos_time[next] = pos_time[now] + 1
                    q.append(next)
            
    time = bfs(soobin)

# 동생 찾는 가장 빠른 시간 출력
print(time)