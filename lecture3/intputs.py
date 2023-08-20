import sys


x = input("x =  ")

y = input("y =  ")

print(x +y) # string 3 + 4 --> 34

z = int(input("z =  "))

zz = int(input("zz =  "))

print(z + zz) # int 3 + 4 --> 7

print("x + y= " +(x + y)) # 에러안나는데?? it cannot print a string concatenated to an integer.
print("x + y= " +str(x + y)) # the result is acceptable

# how can we absorb those two values?
# must import the system module

# ??????????????? sys.argv
# 현재 실행중인 파일의 이름을 반환하는 함수
# return string
a = sys.argv[1]

b = sys.argv[2]

print(a + b) # 22 + 33 --> 2233

aa = float(sys.argv[1])

bb = float(sys.argv[2])

print(aa + bb) # 22 + 33 -> 55