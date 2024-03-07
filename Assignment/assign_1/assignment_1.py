import os, sys
Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#-- Vigenere 암호화
def vigenere_encrypt(key, msg):
    result = ''        
    #암호키(단어)를 리스트로 만든다. (유효성 확인도 추가하자)
    key_list = list(key.upper())
    key_pos= 0        
    for ch in msg:
        if ch.upper() in Alphabet:
            key_ch = Alphabet.find(key_list[key_pos])
            idx = Alphabet.find(ch.upper())
            if ch.isupper():
                result += Alphabet[(idx+key_ch)%26].upper()
            else:
                result += Alphabet[(idx+key_ch)%26].lower()            
        else:
            result += ch
        key_pos = (key_pos + 1) % len(key)
    return result
#=====================
# 파일 암호화
in_file = 'TEXT-1.txt'

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

key = 'KEYISKEY'
CT = vigenere_encrypt(key, PT)

out_file = 'CIPHER-1.txt'
   
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
