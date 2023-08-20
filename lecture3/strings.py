s = "Python is easy 2023"

length = len(s) # returns the length of s

# print("length =" + length) 에러 integer라서  
print("length =" + str(length))

print(s[0]) # "Python is easy 2023" ---> P
print(s[length - 1]) # "Python is easy 2023" ---> 마지막 숫자 3
# print(s[length]) 인덱스 에러

print(s[2:6])
# print(s[(length/2):]) 에러 slice indices must be integers 
print(s[int(length/2):]) # # "Python is easy 2023" --> easy 2023

print(s.count('2')) # 2023에서 2 두번 -> 2출력

print(s.lower())
print(s.upper())

print(s.index('2')) # 반복된다면 첫번째 인덱스만 반환
print(s.replace('easy', 'FSD'))
print(s) # 위에 저장은 안된듯
print(s.find('2'))
print(s.isalpha()) # false출력 : all characters are alphabetical used in the alpha
print(s.isnumeric()) # false 
print(s.isalnum()) # false 숫자+알파벳만 있는지.. we have white space -> false

