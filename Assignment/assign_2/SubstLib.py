Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# 암호화 함수
def subst_encrypt(key, msg): 
    result = ''
    InSet = Alphabet
    OutSet = key
    for ch in msg:
        if ch.upper() in InSet:
            idx = InSet.find(ch.upper()) 
            if ch.isupper():
                result += OutSet[idx].upper()
            else:
                result += OutSet[idx].lower()   
        else:
            result += ch
    return result

# 복호화 함수
def subst_decrypt(key, msg):
    result = ''
    Inset = key
    Outset = Alphabet
    
    for ch in msg:
        if ch.upper() in Inset:
            idx = Inset.find(ch.upper())
            if ch.isupper():
                result += Outset[idx].upper()
            else:
                result += Outset[idx].lower()
        else :
            result += ch 
    return result
    
    