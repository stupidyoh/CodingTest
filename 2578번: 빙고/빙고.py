#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2578                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2578                           #+#        #+#      #+#     #
#    Solved: 2025/07/09 20:33:44 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 주어진 입력받기
board = [list(map(int, input().split())) for _ in range(5)]

# 사회자가 부르는 수
numbers = [list(map(int, input().split())) for _ in range(5)]

# 사회자가 부른 수의 위치 찾기
def find(n):
    for j in range(5):
        for i in range(5):
            if board[j][i] == n:
                return i, j

# 빙고 계산
bingo_type = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 1~5행 빙고, 1~5열 빙고, \ / 빙고 순

# 3개의 선이 만들어지는 턴 찾기
def bingo():
    turn_bingo = 0
    # 부른 수 순서대로 탐색
    for number in numbers:
        for n in number:
            # 사회자가 부른 수 위치
            x, y = find(n)
            turn_bingo += 1
            # 0으로 만들어 체크 표시
            board[y][x] = 0

            # 행방향 빙고
            bingo_col = 0
            for i in range(5):
                if board[y][i] == 0:
                    bingo_col += 1
            if bingo_col == 5:
                bingo_type[y] = 1

            # 열방향 빙고
            bingo_row = 0
            for j in range(5):
                if board[j][x] == 0:
                    bingo_row += 1
            if bingo_row == 5:
                bingo_type[x+5] = 1

            # \ 빙고
            if x == y:
                bingo_dia = 0
                for d in range(5):
                    if board[d][d] == 0:
                        bingo_dia += 1
                if bingo_dia == 5:
                    bingo_type[10] = 1

            # / 빙고
            if x + y == 4:
                bingo_dia_rev = 0
                for d in range(5):
                    if board[d][4-d] == 0:
                        bingo_dia_rev += 1
                if bingo_dia_rev == 5:
                    bingo_type[11] = 1

            # 빙고가 3개 이상이면 빙고 외치기
            if sum(bingo_type) >= 3:
                print(turn_bingo)
                return

bingo()