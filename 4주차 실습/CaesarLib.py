#--------------------------------
# 암호분석 - Caesar 암호 라이브러리
#--------------------------------

UpAlphabet    = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LowAlphabet = 'abcdefghijklmnopqrstuvwxyz'

#== 암호화 함수
def caesar_encrypt(key, plain_msg):    
    cipher_msg = ''
    for symbol in plain_msg:
        if symbol in UpAlphabet:
            cipher_msg +=  UpAlphabet[ (UpAlphabet.find(symbol)+key)%26 ]
        elif symbol in LowAlphabet:
            cipher_msg +=  LowAlphabet[ (LowAlphabet.find(symbol)+key)%26 ]
        else:
            cipher_msg += symbol
    return cipher_msg


#== 복호화 함수
def caesar_decrypt(key, cipher_msg):    
    recovered_msg = ''
    for symbol in cipher_msg:
        if symbol in UpAlphabet:
            recovered_msg +=  UpAlphabet[ (UpAlphabet.find(symbol)-key)%26 ]
        elif symbol in LowAlphabet:
            recovered_msg +=  LowAlphabet[ (LowAlphabet.find(symbol)-key)%26 ]
        else:
            recovered_msg += symbol
    return recovered_msg

#== 라이브러리 동작을 확인하기 위한 함수
def main():
    print("Test Run for Caesar Cipher")
    
    PT = "This is a plaintext."
    key = 3
    CT = caesar_encrypt(key, PT)
    print('PT =', PT)
    print('CT =', CT)
    recovered_PT = caesar_decrypt(key, CT)
    print('Recovered PT =', recovered_PT)
    
#========
# 라이브러리를 실행하면 main() 함수가 호출된다.

if __name__ == '__main__':
    main()