'''
========================================================================

암호분석 - TC20 MITM attack ( 이중 암호화에 대한 )

공격조건 : 기지평문공격 (Known plaintext attack)
(평문, 암호문) 쌍을 수집하여 키를 찾는 공격 (2쌍 정도 필요)

암호 알고리즘 (double encryption)

CT  = E ( E (pt, ket1), key2)
PT  -- [E, key1] ---> Mid -- [E, key2] --> CT

CT = E(P, key) 는 취약한 경우
키를 2개 사용하여 이중 암호화하면 안전할까?

키 전수조사 : 2^ k --> 2^(k+k) (k: 키의 비트 수)
MITM attack : 2^(k+1) 의 공격으로 이중암호화를 해독가능

PT --> [E, key1] --> Mid (모든 key1에 대해 계산하고 저장)
CT --> [E, key2] --> Mid' (모든 key2에 대해 계산하고 저장된 값과 비교)
Mid' == Mid 이면 key1, key2 가 후보키로 등록한다.
키가 정확한지 다른 평문 ,암호문 쌍을 이용하여 확인한다.

========================================================================
'''
import TC20_lib as TC20 # TC20.Enc... 줄여서 쓰기 가능
import pickle # 데이터를 파일로 저장하기 위함


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

# 변수를 파일에 저장
def save_var_to_file(var, filename):
    f = open(filename, 'w+b')
    # File error...
    pickle.dump(var, f)
    f.close()
    
# 변수를 파일에서 읽기
def load_var_from_file(filename):
    f = open(filename, 'rb')
    var = pickle.load(f)
    f.close()
    return var

#========================================================================

#========================================================================
# MITM 공격용 샘플 만들기

'''
key1 = [0, 1, 2, 3]
key2 = [0, 4, 5, 6]

PT1 = [0, 10, 20, 30]
mid1 = TC20.TC20_Enc(PT1, key1)
CT1 = TC20.TC20_Enc(mid1, key2)

PT2 = [0, 40, 50, 60]
mid2 = TC20.TC20_Enc(PT2, key1)
CT2 = TC20.TC20_Enc(mid2, key2)

print('key1 = ' , key1)
print('key2 = ' , key2)

print('PT1 = ' , PT1)
print('mid1 = ', mid1)
print('CT1 = ', CT1)

print('PT2 = ' , PT2)
print('mid2 = ', mid2)
print('CT2 = ', CT2)

'''
# 평문 pt 입력 받아 모든 key1으로 암호화한 결과를 사전으로 저장
# dic = { (mid1, k1) , (mid2 , k2), .... }
def make_mid_dic(pt):
    dic = {} # empty dictionary
    print('Making encryption dictionary', end='')
    N = 1 << 24 # 24bit key1
    for idx in range(N):
        key = int2list(idx) # 카운터 변수(정수) - > 암호키 (리스트)로
        mid = TC20.TC20_Enc(pt, key)
        int_mid = list2int(mid) # 사전 { ( key, value )} 에서 key를 정수로 
        int_key = idx # 정수로 표현한 암호키값
        
        if int_mid in dic: # 사전에 있는 mid 값인지?
            dic[int_mid].append(int_key)
        else :
            dic[int_mid] = [ int_key ]
        #dic [00 00 00 00] = [ 0***, 0@@@, ... ]

        if (idx %(1 <<16)) == 0:
            print('.', end= ' ')
    print("done")
    return dic

# ======= 
# [MITM 1단계] 사전 만들기

# dic = {(mid1, k1) , (mid2, k2), (mid3, k3) .... }
# dic[mid3] = k3 참조하는 방법
'''
PT1 = [0, 10, 20, 30]
mid_dic = make_mid_dic(PT1)
save_var_to_file(mid_dic, 'mid.dic')
'''

# ======= 
# [MITM 2단계] 암호문 - > 중간값 (mid')

mid_dic = load_var_from_file('mid.dic')
N = 1 << 24

PT1 = [0, 10, 20, 30]
CT1 = [74, 22, 29, 142]
PT2 = [0, 40, 50, 60]
CT2 = [7, 40, 163, 67]
print('Load dic file')

for idx in range(N):
    key2 = int2list(idx)
    mid_ct = TC20.TC20_Dec(CT1, key2) 
    int_mid_ct = list2int(mid_ct)
    if int_mid_ct in mid_dic: # CT1으로부터 계산한 mid 가 사전에 있는지?
        # 두번째 평문 암호문 쌍으로 확인
        key1 = int2list(mid_dic[int_mid_ct][0])
        # mid_dic[int_mid_ct] = [ k0, k1, ....]
        mid2 = TC20.TC20_Enc(PT2, key1)
        ct2_calc = TC20.TC20_Enc(mid2, key2)
        if ct2_calc == CT2:
            print('key1 = ', key1)
            print('key2 = ', key2)
        print('key2 =', key2)
        
    if (idx % (1<<16) == 0):
        print('.', end='')
print('key search completed.')
        


    
