#--------------------------
# 암호분석 - VigenereLib 암호 라이브러리를 이용한 파일 암복호화 예제
#--------------------------

import VigenereLib
import os, sys
import EngDicLib # IC(Index of Coincidence) 함수

#=====================
# 파일 암호화

in_file = 'PT3.txt'

if not os.path.exists(in_file):
    print("Working directory:", os.getcwd())
    print('File %s does not exist.' %(in_file))
    sys.exit()  # 프로그램 종료
    
#-- 입력파일에서 읽기
InFileObj = open(in_file)    
PT = InFileObj.read()
InFileObj.close()

print('input file (%s) : ' %(in_file), end = '')
print(PT[:10],"...", PT[-10:])

#-- 암호문 만들기

key = 'MATH'
CT = VigenereLib.vigenere_encrypt(key, PT)

out_file = 'CT3.txt'
   
#-- 출력파일이 존재하면 덮어쓸지 물어보기
if os.path.exists(out_file):
    print('This will overwrite the file %s. (C)ontinue or (Q)uit' % (out_file))
    response = input('> ')    # 사용자 입력 기다리기
    if not response.lower().startswith('c'): 
        sys.exit()

OutFileObj = open(out_file, 'w')
OutFileObj.write(CT)
OutFileObj.close()

print('Output file (%s) : ' %(out_file), end='')
print(CT[:10], '...', CT[-10:])

#=====================
# 파일 복호화

in_file = 'CT3.txt'

if not os.path.exists(in_file):
    print("Working directory:", os.getcwd())
    print('File %s does not exist.' %(in_file))
    sys.exit()  # 프로그램 종료
    
#-- 입력파일에서 읽기
InFileObj = open(in_file)    
CT = InFileObj.read()
InFileObj.close()

print('input file (%s) : ' %(in_file), end = '')
print(CT[:10],"...", CT[-10:])

#-- 복호파일 만들기

key = 'MATH'
recPT = VigenereLib.vigenere_decrypt(key, CT)

out_file = 'recPT3.txt'
   
#-- 출력파일이 존재하면 덮어쓸지 물어보기
if os.path.exists(out_file):
    print('This will overwrite the file %s. (C)ontinue or (Q)uit' % (out_file))
    response = input('> ')    # 사용자 입력 기다리기
    if not response.lower().startswith('c'): 
        sys.exit()

OutFileObj = open(out_file, 'w')
OutFileObj.write(recPT)
OutFileObj.close()

print('Output file (%s) : ' %(out_file), end='')
print(recPT[:10], '...', recPT[-10:])

print('IC(PT)= %6.4f' %(EngDicLib.IC(PT)))
print('IC(CT)= %6.4f' %(EngDicLib.IC(CT)))
