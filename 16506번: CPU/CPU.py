#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 16506                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: gattswet0926 <boj.kr/u/gattswet0926>        +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/16506                          #+#        #+#      #+#     #
#    Solved: 2025/05/15 10:37:30 by gattswet0926  ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# v2
# 코드 간결화

import sys

opcode_map = {
    "ADD": "0000", "SUB": "0001", "MOV": "0010", "AND": "0011",
    "OR": "0100", "NOT": "0101", "MULT": "0110", "LSFTL": "0111",
    "LSFTR": "1000", "ASFTR": "1001", "RL": "1010", "RR": "1011"
}

def to_binary(num, width):
    return bin(int(num))[2:].zfill(width)

def convert_to_machine_code(opcode, rD, rA, rB):
    # 기본 opcode 및 C 여부 추출
    base_opcode = opcode.rstrip("C")
    is_immediate = opcode[-1] == "C"
    
    # 기계어 코드 구성
    machine_code = opcode_map[base_opcode]
    machine_code += "10" if is_immediate else "00"
    machine_code += to_binary(rD, 3)
    
    # rA 처리 (MOV, NOT 명령어는 특별 처리)
    if base_opcode in ["MOV", "NOT"]:
        machine_code += "000"
    else:
        machine_code += to_binary(rA, 3)
    
    # rB/immediate 값 처리
    if is_immediate:
        machine_code += to_binary(rB, 4)
    else:
        machine_code += to_binary(rB, 3) + "0"
    
    return machine_code

# 메인 프로그램
num_command = int(input())
for _ in range(num_command):
    opcode, rD, rA, rB = sys.stdin.readline().split()
    machine_code = convert_to_machine_code(opcode, rD, rA, rB)
    print(machine_code)


#  **************************************************************************  #

# v1
# 단순 구현

# import sys

# opcode_library = {
#     "ADD" : "0000", "ADDC" : "0000",
#     "SUB" : "0001", "SUBC" : "0001",
#     "MOV" : "0010", "MOVC" : "0010",
#     "AND" : "0011", "ANDC" : "0011",
#     "OR" : "0100", "ORC" : "0100",
#     "NOT" : "0101",
#     "MULT" : "0110", "MULTC" : "0110",
#     "LSFTL" : "0111", "LSFTLC" : "0111",
#     "LSFTR" : "1000", "LSFTRC" : "1000",
#     "ASFTR" : "1001", "ASFTRC" : "1001",
#     "RL" : "1010", "RLC" : "1010",
#     "RR" : "1011", "RRC" : "1011",
# }

# # 주어진 입력받기
# num_command = int(input())
# for _ in range(num_command):
#     opcode, rD, rA, rB = map(str, sys.stdin.readline().split())
#     machine = ""

#     # opcode & 5bit
#     machine += opcode_library[opcode]
#     if opcode[-1] == "C":
#         machine += "10"
#     else:
#         machine += "00"

#     # rD
#     machine += str(bin(int(rD)))[2:].zfill(3)

#     # rA
#     if opcode == "MOV" or opcode == "MOVC" or opcode == "NOT":
#         machine += "000"
#     else:
#         machine += str(bin(int(rA)))[2:].zfill(3)

#     # rB 또는 #C
#     if opcode[-1] == "C":
#         machine += str(bin(int(rB)))[2:].zfill(4)
#     else:
#         machine += str(bin(int(rB)))[2:].zfill(3)
#         machine += "0"

#     print(machine)