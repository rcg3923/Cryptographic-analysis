###

"""

 Caesar 암호 함수 라이브러리 : CaesarLib
 
 """
####

UpAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LowAlphabet = 'abcdefghijklmnopqrstuvwxyz'


def Caesar_Enc(Key, PT):
    #Cipher Text
    CT = ' '
    
    for ch in PT:
        if ch in UpAlphabet:
            new_idx = (UpAlphabet.find(ch) + Key) % 26
            CT = CT + UpAlphabet[new_idx]
        elif ch in LowAlphabet:
            new_idx = (LowAlphabet.find(ch) + Key) % 26
            CT = CT + LowAlphabet[new_idx]
        else:
            CT = CT + ch # 대문자, 소문자가 아니면 그대로 추가한다.
    return CT
 
def Caesar_Dec(Key, CT):
    #주어진 암호문 CT를 복호화하여 recPT를 만들자
    recPT = ''

    for ch in CT:
        if ch in UpAlphabet:
            new_idx = (UpAlphabet.find(ch) - Key) % 26
            recPT += UpAlphabet[new_idx]
        elif ch in LowAlphabet:
            new_idx = (LowAlphabet.find(ch) - Key) % 26
            recPT += LowAlphabet[new_idx]
        else:
            recPT = recPT + ch # 대문자, 소문자가 아니면 그대로 추가한다.
    return recPT




def main():
    #plain Text
    PT = "I have an apple."
    key = 3 # Encrypto key

    CT = Caesar_Enc(key, PT)
    print('Plain Text : ',PT)
    print('Cipher Text : ', CT)

    recPT = Caesar_Dec(key, CT)
    print('Cipher Text :' , CT)
    print('Plain Text :', recPT)

# 라이브러리를 실행하면 main() 함수가 호출되고
# Import 하여 사옹할 때는 main() 함수가 실행되지 않게 하자

if __name__ == '__main__' :
    main()