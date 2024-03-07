#--------------------------
# 암호분석 - Vigenere 암호 라이브러리
#--------------------------
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

#-- Vigenere 복호화
def vigenere_decrypt(key, msg):
    result = ''        
    #암호키(단어)를 리스트로 만든다. (유효성 확인도 추가하자)
    key_list = list(key.upper())
    key_pos= 0        
    for ch in msg:
        if ch.upper() in Alphabet:
            key_ch = Alphabet.find(key_list[key_pos])
            idx = Alphabet.find(ch.upper())
            if ch.isupper():
                result += Alphabet[(idx-key_ch)%26].upper()
            else:
                result += Alphabet[(idx-key_ch)%26].lower()
        else:
            result += ch
        key_pos = (key_pos + 1) % len(key)
    return result

#=== 라이브러리 동작확인을 위한 함수 
def main():
    print("SubstCipherLib test...")
    my_key = 'ABCD'
    msg1 = "What is Caesar cipher? Is it secure?"
    CT = vigenere_encrypt(my_key, msg1)
    print('msg =', msg1)
    print('key =', my_key)
    print('ciphertext =', CT)
    recPT = vigenere_decrypt(my_key, CT)
    print('recPT =', recPT)
#========
if __name__ == '__main__':
    main()