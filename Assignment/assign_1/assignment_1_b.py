#--------------------------
# 암호분석 - VigenereLib 암호의 공격방법
#--------------------------
import VigenereLib, CaesarLib
import os, sys
import EngDicLib # IC(Index of Coincidence) 함수

#===[1]
# 패스워드(암호키) 길이를 찾는 공격
in_file = 'CIPHER-1.txt'

if not os.path.exists(in_file):
    print("Working directory:", os.getcwd())
    print('File %s does not exist.' %(in_file))
    sys.exit()  # 프로그램 종료
    
#-- 입력파일에서 읽기
InFileObj = open(in_file)    
CT = InFileObj.read()
InFileObj.close()

print('input file (%s) : ' %(in_file), end = '')
print(CT[:10],"...", CT[-10:], '( length =', len(CT), ')')

MAX_KEY_LENGTH = 8 # 암호키의 최대길이 설정(가정)

keylen_candidate = 0
max_ic = 0.0
for key_len in range(1,MAX_KEY_LENGTH+1):
    sub_msg = ''
    idx = 0
    while idx < len(CT):
        sub_msg += CT[idx]
        idx += key_len
    
    sub_ic = EngDicLib.IC(sub_msg) 
    if max_ic < sub_ic:
        max_ic = sub_ic
        keylen_candidate = key_len
    print('key_len =', key_len, ':', end='')
    print('sub_msg', sub_msg[:10],"...", '( length =', len(sub_msg), ')\t', end='')
    print('IC(sub_msg)= %6.4f' %(sub_ic))
    
# 찾은 키 길이 출력
print('key length =', keylen_candidate)

#===[2]
# 찾은 키 길이가 맞을때 키 찾기 -- 원리 설명용 (CT[i], CT[i+1]) 
key_list = [0]*keylen_candidate

key_ch_candidate = 0
max_ic = 0.0
for key_ch in range(0,26): 
    sub_msg = ''
    idx = 0
    while idx < len(CT):
        sub_msg += CT[idx]
        if (idx+1) < len(CT):
            sub_msg += CaesarLib.caesar_decrypt(key_ch, CT[idx+1])
        idx += keylen_candidate

    sub_ic = EngDicLib.IC(sub_msg)
    if max_ic < sub_ic:
        max_ic = sub_ic
        key_ch_candidate = key_ch
        
    print('key_ch =', key_ch, ':', end='')
    print('sub_msg', sub_msg[:10],"...", '( length =', len(sub_msg), ')\t', end='')
    print('IC(sub_msg)= %6.4f' %(sub_ic))
    
print('key_ch_candidate =', key_ch_candidate)

#===[3]
# 키 길이를 이용하여 키를 찾는 공격법 (1단계: 키의 상대적 인덱스)

key_list = [0]*keylen_candidate

for key_pos in range(1,keylen_candidate):
    key_ch_candidate = 0
    max_ic = 0.0
    for key_ch in range(0,26): 
        sub_msg = ''
        idx = 0
        while idx < len(CT):
            sub_msg += CT[idx]
            if (idx+key_pos) < len(CT):
                sub_msg += CaesarLib.caesar_decrypt(key_ch, CT[idx+key_pos])
            idx += keylen_candidate
    
        sub_ic = EngDicLib.IC(sub_msg)
        if max_ic < sub_ic:
            max_ic = sub_ic
            key_ch_candidate = key_ch
            
        #print('key_ch =', key_ch, ':', end='')
        #print('sub_msg', sub_msg[:10],"...", '( length =', len(sub_msg), ')\t', end='')
        #print('IC(sub_msg)= %6.4f' %(sub_ic))
    
    key_list[key_pos] = key_ch_candidate
    print('key[%d] : key_ch_candidate = %d' %(key_pos, key_ch_candidate))
    
    
#===[4]
# 키 길이를 이용하여 키를 찾는 공격법 (2단계: 키 찾기)

key_0_candidate = -1

for key_ch in range(0,26): 
    dec_msg = ''
    key_pos= 0
    for ch in CT:
        key_now = (key_ch + key_list[key_pos]) % 26
        dec_msg += CaesarLib.caesar_decrypt(key_now, ch)        
        key_pos = (key_pos + 1) % keylen_candidate

    eng_percent = EngDicLib.percentEnglishWords(dec_msg)
        
    print('key_ch =', key_ch, ':', end='')
    print('dec_msg', dec_msg[:10],"...", '( length =', len(dec_msg), ')\t', end='')
    print('Eng(dec_msg)= %5.2f %%' %(eng_percent*100))

    if EngDicLib.isEnglish(dec_msg):
        key_0_candidate, rightPT = key_ch, dec_msg

if key_0_candidate >= 0:
    rightkey = ''
    for idx in key_list:
        rightkey += VigenereLib.Alphabet[(key_0_candidate + idx) % 26]
        
    print('right key =', rightkey)
    print('PT = ', rightPT[:20], '...', rightPT[-10:])
    out_file = 'Decode_CIPHER-1.txt'
    OutFileObj = open(out_file, 'w')
    OutFileObj.write(rightPT)
    OutFileObj.close()