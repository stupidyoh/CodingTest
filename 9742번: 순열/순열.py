#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9742                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9742                           #+#        #+#      #+#     #
#    Solved: 2025/07/05 13:01:26 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from math import factorial

def solve(string, i):
    global count
    # 순열이 기존 문자열 길이와 같아지면
    if i == len(testcase):
        count += 1 # 순열 순서 증가
        # 목표 순서에 돌달하면 해당 순서의 순열 문자열 반환
        if count == order:
            return string
    # 기존 문자열 길이보다 짧다면
    else:
        # 입력 문자열을 하나씩 순회
        for s in testcase:
            # 순열 조합 안에 현재 문자가 없다면
            if s not in string:
                # 재귀적으로 계산 b -> be -> bei -> (bein) -> ben -> (beni)
                res = solve(string + s, i + 1)
                # 목표 순열을 찾았을 때 정답 순열 조합 반환, 없다면 None
                if res:
                    return res
    return # 조건 불충족시 None 반환

# 주어진 입력받기
while True:
    try:
        testcase, order = map(str, sys.stdin.readline().split())
        order = int(order)
        count = 0 # 순열 위치 차례대로 카운트
        
        # 주어진 위치에 해당하는 순열이 없는 경우        
        if order > factorial(len(testcase)):
            print(testcase, order, '=', "No permutation")
        # 있는 경우
        else:
            print(testcase, order, '=', solve('', 0))

    except:
        break # 더이상 테스트케이스가 없는 경우