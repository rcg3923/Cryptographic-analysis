import SubstLib
import os, sys

# 이것은 테스트 파일을 만들기 위한 곳 키 대입하는 곳

in_file = 'CIPHER-2.txt'

if not os.path.exists(in_file):
    print("Working directory:", os.getcwd())
    print('File %s does not exist.' %(in_file))
    sys.exit()  # 프로그램 종료
    
#-- 암호화 파일 불러들이기
InFileObj = open(in_file)    
CT = InFileObj.read()
InFileObj.close()
# -----------------------------------
test_CT = CT
Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# 영문자 빈도순서
ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

mapping = {'A': '_', 'B' : '_', 'C' : '_', 'D' : '_', 'E' : '_', 'F' : '_', 'G' : '_', 'H' : '_', 
          'I' : '_', 'J' : '_', 'K' : '_', 'L' : '_', 'M' : '_', 'N' : '_', 'O' : '_', 'P' : '_', 
          'Q' : '_', 'R' : '_', 'S' : '_', 'T' : '_', 'U' : '_', 'V' : '_', 'W' : '_', 'X' : '_', 'Y' : '_', 'Z' : '_',}

# 1 번째 키
# 이름을 이렇게 지은 것은 똑같은 자리를 판별하기 위함
cipher_test = 'TKAQVZPGWDHUNSYXOMFLRCIBEJ'
candida_key = 'ETONKIFLRYAMSHWCVDPZUJGQXB'

# 2 번째 키
# 이름을 이렇게 지은 것은 똑같은 자리를 판별하기 위함
cipher_test_2 = 'VPAUGDQYOZWSKLCBHRTMJENXIF'
candida_key_2 = 'TESOIANRULHCPYDFBGMWVKJXQZ'

for i in range(len(cipher_test_2)):
    mapping[cipher_test_2[i]] = candida_key_2[i]
for ch in test_CT:
    if ch.upper() in Alphabet:
        print(mapping[ch.upper()], end='')
    else:
        print(ch, end='')
        
# 현재 mapping 테스트
print('\n',mapping)