###

"""

 Caesar 암호 함수
 
 """
####


UpAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LowAlphabet = 'abcdefghijklmnopqrstuvwxyz'


def Caesar_Enc(Key, PT):
    #Cipher Text
    CT = ' '
    
    for ch in PT:
        if ch in UpAlphabet:
            new_idx = (UpAlphabet.find(ch) + key) % 26
            CT = CT + UpAlphabet[new_idx]
        elif ch in LowAlphabet:
            new_idx = (LowAlphabet.find(ch) + key) % 26
            CT = CT + LowAlphabet[new_idx]
        else:
            CT = CT + ch # 대문자, 소문자가 아니면 그대로 추가한다.
    return CT
 
def Caesar_Dec(Key, CT):
    #주어진 암호문 CT를 복호화하여 recPT를 만들자
    recPT = ''

    for ch in CT:
        if ch in UpAlphabet:
            new_idx = (UpAlphabet.find(ch) - key) % 26
            recPT += UpAlphabet[new_idx]
        elif ch in LowAlphabet:
            new_idx = (LowAlphabet.find(ch) - key) % 26
            recPT += LowAlphabet[new_idx]
        else:
            recPT = recPT + ch # 대문자, 소문자가 아니면 그대로 추가한다.
    return recPT

    
#plain Text
PT = "I have an apple."
key = 3 # Encrypto key

CT = Caesar_Enc(key, PT)
print('Plain Text : ',PT)
print('Cipher Text : ', CT)

recPT = Caesar_Dec(key, CT)
print('Cipher Text :' , CT)
print('Plain Text :', recPT)



 
 
 