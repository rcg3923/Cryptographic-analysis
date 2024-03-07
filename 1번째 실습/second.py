###

"""

 Caesar 암호 기본 
 
 """
 ####
 
UpAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LowAlphabet = 'abcdefghijklmnopqrstuvwxyz'
 
#plain Text
PT = "I have an apple."
 
key = 3 # Encrypto key
 
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

print('Plain Text : ',PT)
print('Cipher Text : ', CT)


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
        
print('Cipher Text :' , CT)
print('Plain Text :', recPT)


 
 
 