'''
암호분석 - Caesar 암호 라이브러리를 이용한 암호화 예제

'''

import caesar_lib as Caesar

#plain Text

PT = "I have an apple."
key = 3 # Encrypto key

CT = Caesar.Caesar_Enc(key, PT)
print('Plain Text : ',PT)
print('Cipher Text : ', CT)

recPT = Caesar.Caesar_Dec(key, CT)
print('Cipher Text :' , CT)
print('Plain Text :', recPT)
