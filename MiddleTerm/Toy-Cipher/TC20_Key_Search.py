
'''
암호분석 - TC 20 키 전수조사 공격법

공격조건 : 기지평문공격(known plaintext attack)
 평문, 암호문 쌍을 수집하여 키를 찾는 공격
 
'''

import TC20_lib as TC20 # TC20.Enc... 줄여서 쓰기 가능



# Function 데이터 변환 함수

# ex : 0x12345678 ( 4 바이트 정수) --> [0x12, 0x34, 0x56, 0x78] (리스트)
# 카운터 (정수) --> 암호키 (리스트)
def int2list(n):
    out_list = []
    out_list.append( (n >> 24) &0xff ) #0x12 & 0xff
    out_list.append (( n >> 16) & 0xff) #0x1234 & 0xff = 0x34
    out_list.append ((n >> 8) & 0xff) # 0x123456 & 0xff = 0x56
    out_list.append ( n & 0xff ) # 0x12345678 & 0xff = 0x78
    return out_list

# 예 : [0x12, 0x34 ,0x56, 0x78] (리스트) --> 0x12346578 (4byte integer)
# Key(list) 를 카운터 (정수) 로 변환할 때 사용

def list2int(l): # l = list
    n = 0
    num_byte = len(l)
    for idx in range(len(l)): #리스트에서 한 바이트씩 선택
        # 0x12 --> 0x12 00 00 00 =  0x12 << 24 list의 길이만큼 (24 = 8 * (길이 (바이트 수) - 1) )
        n += l[idx] << 8 * (num_byte - idx - 1)
    return n

# ================================================================================================

# 공격 연습용 샘플 만들기

# ================================================================================================
# 공격 연습용 샘플 만들기 (pt, ct) 암호키 k = [0, *, *, *] (24  비트만 사용 가능)



# ===============================================
# 키 전수조사 공격
given_pt = [0, 10, 20, 30]
given_ct = [26, 2, 201, 171]

# Flag = False # 키를 찾으면 True로 설정할 변수
KeySize = 1 << 24 # 24비트 키 공간을 탐색 ( 2 ^ 24)
Key_list = [] # 키 후볼르 저장할 리스트

print('Key Search Start ', end =' ')
for idx in range (0, KeySize):
    key_guess = int2list(idx)
    pt = TC20.TC20_Dec(given_ct, key_guess)
    if pt == given_pt: # Search to Key_guess
        Key_list.append(key_guess) # Key list append and 계속탐색   
    if (idx % (1 << 16) == 0):
        print('.', end= '')
        
print('\n')
print('key = ', Key_list)
if len(Key_list) == 0:
    print('key not found')