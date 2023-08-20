x = 2
print(x)
print(type(x))

x = True
print(x)
print(type(x))

x = "Hello"
print(x)
print(type(x))

x = 2
y = 3.5

x += 1 #    x = x + 1
x -= y #    x = x - y
x /= 3
x *= 2
x %= 2

print(f'{x**2:.3f}') # specify how many decimal points I want 

z = 2
print(z)
zz = z**2 # 제곱
print(zz)

print(x is not y) # bullean 
print(not(x is y)) # 같은 결과
print(not(x == y)) 

b = (x >= y or not(x != y)) and (x is y or (x < y))

print(b)


