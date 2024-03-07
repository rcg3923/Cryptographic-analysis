#
# --- Python 데이터 변환 --- 
#

# 1byte = 8 bits -> 256가지 2^8
# 10 진수 0 ~ 255
# 16 진수 0x00 ~ 0xFF
# ASCII 문자 : 7 비트로 표현  0|7bits

#  65 = 4 x 16 + 1 = 16진수로 0x41 이 된다 아스키코드로 = 'A'

'''
ch1 = 'A'
num1 = ord(ch1)
hex1 = hex(num1)
bin1 = format(num1, 'b')


print(ch1) # 'A'
print(num1) # 65 는 정수
print(hex1) #0x41 은 문자열 '0x41'
print('bin1 = ', bin1)

# list : 배열처럼 사용가능 
# list : 서로 다른 종류의 데이터를 모을 수 있다.

list1 =[]

list1.append(ch1)
list1.append(num1)
list1.append(hex1)
list1.append(bin1)

print(list1)
'''

'''

str2 = 'ABCD'
list2 = list(str2)
list3 = [ord(ch) for ch in str2]
list4 = [hex(ord(ch)) for ch in str2 ]# hex
list5 = [format(ord(ch), 'b') for ch in str2]# binary

list6 = [128, 129, 130, 65, 66, 67]
list7 = [chr(num) for num in list6]



print(list2)
print(list3)
print(list4)
print(list5)

print(list6)
print(list7)

'''

'''
str8 = 'ABCD'
byte8 = bytes(str8, 'ascii')
print('byte8 =', byte8)
str9 = byte8.decode('ascii')
print(str9)

'''
# ASCII(utf-8) -- [encoding] --> byte
# byte -- [decoding] --> ASCII (utf-8)


# 파일 입출력

f = open('data-1.bin', 'w+b') # 바이너리 (8비트까지 출력)
list11 = [1,2,3, 65, 66, 67, 68, 128]
byte11 = bytes(list11)
print('byte11 = ', byte11) # --> byte11 = b'ABCD' b는 byte들의 모임이다
f.write(byte11)
f.close()
