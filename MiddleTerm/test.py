Alpha_Numeric = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789'

# Encrypto Function

def subst_encrypt(key , msg):
    result = ''
    Inset = Alpha_Numeric
    Outset = key
    
    for ch in msg:
        if ch.upper() in Inset:
            idx = Inset.find(ch.upper())
            if ch.isupper():
                result += Outset[idx].upper()
            else :
                result += Outset[idx].lower()
    return result

# Decrypt Function

def subst_decrypt(key, msg):
    result = ''
    Inset = key
    Outset = Alpha_Numeric
    
    for ch in msg:
        if ch.upper() in Inset:
            idx = Inset.find(ch.upper())
            if ch.isupper():
                result += Outset[idx].upper()
            else :
                result += Outset[idx].lower()
    return result
mykey = '2QCA5ZOIJW1EUHB7 TYRVFD34OLX96MK8GSNP'

PT = 'ACE'
CT = subst_encrypt(mykey, PT)

print('PT = ', PT)
print('CT = ', CT)