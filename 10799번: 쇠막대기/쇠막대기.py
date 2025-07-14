#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10799                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10799                          #+#        #+#      #+#     #
#    Solved: 2025/07/14 17:56:10 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 주어진 입력받기
batchs = input()

stack = []
i = 0 # 입력 문자열 인덱스
num_piece = 0 # 잘려진 조각 개수

while i < len(batchs):
    # 스택 없고 레이저가 아닐 때, 스택 추가
    if not stack and batchs[i+1] != ")":
        stack.append(batchs[i])
        i += 1
        continue

    if batchs[i] == "(":
        # 레이저일 경우, 스택만큼 잘린 조각 추가 + 다음 순서 건너뛰기
        if batchs[i+1] == ")":
            num_piece += len(stack)
            i += 2
        # 막대일 경우, 스택 추가
        else:
            stack.append(batchs[i])
            i += 1
    # 막대 끝부분일 경우, 스택 줄이고 잘린 끝조각 1 추가
    else:
        stack.pop()
        num_piece += 1
        i += 1

# 잘려진 조각의 총 개수 출력
print(num_piece)