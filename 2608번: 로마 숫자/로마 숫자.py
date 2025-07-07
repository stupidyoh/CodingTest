#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2608                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2608                           #+#        #+#      #+#     #
#    Solved: 2025/07/07 18:57:27 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 주어진 입력받기
num1 = input()
num2 = input()

# 로마 숫자 -> 아라비아 숫자
rome = {
    "IV" : 4,
    "IX" : 9,
    "XL" : 40,
    "XC" : 90,
    "CD" : 400,
    "CM" : 900,
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}

def rome2arab(number):
    arab = 0
    i = 0
    while i < len(number):
        if i < len(number)-1:
            if rome[number[i]] >= rome[number[i+1]]:
                arab += rome[number[i]]
            else:
                arab += rome[number[i]+number[i+1]]
                i += 1
        else:
            arab += rome[number[i]]
        i += 1

    return arab

# 숫자 합
arab_sum = rome2arab(num1) + rome2arab(num2)

# 아라비아 숫자 -> 로마 숫자
def arab2rome(number):
    rome_sum = ""
    for s in ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]:
        if number == 0:
            break
        i, number = divmod(number, rome[s])
        rome_sum += s * i

    return rome_sum

# 정답 출력
print(arab_sum)
print(arab2rome(arab_sum))