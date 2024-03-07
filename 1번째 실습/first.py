# Python practice
'''
str1 = "Hello, Python"
print(str1)
print(str1[0:4]) # [a,b] --> a, a+1, ... , b -1
print(str1[-6:]) # 마지막 6글자


msg = "abcdefghijklmnopqrstuvwxyz"

print(msg[0 : 26])
print(msg.find('xyz')) # -> 23
print(msg.find("zz")) # -> -1 (Not find)
'''


# Make Function

'''
def myfunc1(x, y):
    print('myfunc1: x, y = ', x, y, id(x), id(y))
    z = x*y
    print('myfunc1: x, y = ', x, y, id(x), id(y))
    return z

def myfunc2(x, y):
    print('myfunc2: x, y = ', x, y, id(x), id(y))
    x = x*y
    print('myfunc2: x, y = ', x, y, id(x), id(y))
    return x

# print(myfunc1(2,4))

a = 2
b = 1
c = myfunc1(a,b)
print('a, b, c = ', a, b, c)

c = myfunc2(a,b)
print('a, b, c = ', a, b, c)

'''

# 함수 파라미터 전달 방법
# 1) - call by value (c언어) : 파라미터 값을 복사하여 전달하는 방식
# 2) - call by reference (오래된 언어) : 파라미터 위치를 전달하는 방식
# 3) - call by object || reference (Python 방식) : value/reference 방식 혼용





 #- swap() Function

def swap(x, y):
    temp = x
    x = y
    y = temp
    return x,y
    
a = 10
b = 20

print('a, b = ', a, b)
# a,b = swap(a,b)
a, b = b,a
print('a, b = ', a, b)