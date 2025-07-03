#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2304                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2304                           #+#        #+#      #+#     #
#    Solved: 2025/07/03 18:49:41 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# v2: 가장 높은 기둥 기준으로 좌 우 따로 계산

import sys

# 주어진 입력받기
num_column = int(input())
columns = [list(map(int, sys.stdin.readline().split())) for _ in range (num_column)]
columns.sort(key= lambda x: x[0])

max_h = 0
max_h_idx = 0
# 최대 높이 기둥의 위치 찾기
for i in range(num_column):
    if columns[i][1] > max_h:
        max_h = columns[i][1]
        max_h_idx = i

# 최대높이 * 1(너비)
area = max_h

# 왼쪽 끝에서 최대 높이 기둥까지는 증가만 해야함
for i in range(max_h_idx):
    if i == 0:
        temp_max_column = columns[i]

    if columns[i+1][1] >= temp_max_column[1]:
        area += (columns[i+1][0] - temp_max_column[0]) * temp_max_column[1]
        temp_max_column = columns[i+1]

# 최대 높이 기둥에서 오른쪽 끝까지는 감소만 해야함
for i in range(num_column - 1, max_h_idx, -1):
    if i == num_column - 1:
        temp_max_column = columns[i]

    if columns[i-1][1] >= temp_max_column[1]:
        area += (temp_max_column[0] - columns[i-1][0]) * temp_max_column[1]
        temp_max_column = columns[i-1]
        
print(area)
    
    










#  **************************************************************************  #

# v1: 스택(실패)

# import sys

# # 주어진 입력받기
# num_column = int(input())
# columns = [list(map(int, sys.stdin.readline().split())) for _ in range (num_column)]
# columns.sort(key= lambda x: x[0])

# # 지붕을 받치는 주기둥, 주기둥 중 최대높이
# main_column = []
# max_height = 0

# for column in columns:
#     # 스택에 아무것도 없으면 채우기
#     if main_column == []:
#         main_column.append(column)
#         max_height = column[1]
#         continue

#     # 이번 기둥 높이가 직전 기둥보다 낮거나 같으면 스택에 추가
#     if column[1] <= main_column[-1][1]:
#         main_column.append(column)

#     # 이번 기둥 높이가 직전 기둥보다 높으면
#     else:
#         # 스택 탐색(오목한 부분 삭제)
#         while True:
#             # 마지막 스택이 스택 내 최대 높이보다 낮으면 삭제
#             if main_column[-1][1] < column[1] :
#                 main_column.pop()
#             else:
#                 break

#         # 이번 기둥은 스택에 추가
#         main_column.append(column)

#         # 이번 기둥 높이가 스택 내 최대 높이보다 높으면 갱신
#         if column[1] > max_height:
#             max_height = column[1]

# # 창고 면적 초기화
# area = 0

# # 창고 면적 계산
# for i in range(1, len(main_column)):
#     # 현재 높이가 이전보다 같거나 높으면
#     if main_column[i][1] >= main_column[i-1][1]:
#         area += (main_column[i][0] - main_column[i-1][0]) * main_column[i-1][1]
#     # 현재 높이가 이전보다 낮으면
#     else:
#         area += (main_column[i][0] - main_column[i-1][0]) * main_column[i][1]
# # 가장 높은 기둥에 대해 기둥 면적만큼 더하기
# area += max_height

# # 창고 다각형의 면적 출력
# print(area)