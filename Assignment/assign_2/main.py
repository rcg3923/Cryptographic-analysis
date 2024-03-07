import SubstLib
import os, sys
import random
import time

'''

# key를 랜덤하게 만들어야함.
def random_key():
    Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    random.seed(time.time())
    #문자열 알파벳을 랜덤하게 셔플해주고, 다시 문자열로 붙여주는 알고리즘
    alphabet_list = list(Alphabet)
    random.shuffle(alphabet_list)
    rand_message = ''.join(alphabet_list)
    print(rand_message)
    return rand_message

# 유효성 검사 함수
def correct_key(my_key):
    for i in range(26):
        list_key = list(my_key)
        for j in range(i+1, 26):
            if list_key[i] == list_key[j]:
                return False
    return True
              
my_key = random_key()
print(correct_key(my_key))
#=====================
# 파일 암호화
in_file = 'TEXT-1.txt'

if not os.path.exists(in_file):
    print("Working directory:", os.getcwd())
    print('File %s does not exist.' %(in_file))
    sys.exit()  # 프로그램 종료
'''
    
'''

#-- 입력파일에서 읽기
InFileObj = open(in_file)    
PT = InFileObj.read()
InFileObj.close()

print('input file (%s) : ' %(in_file), end = '')
print(PT[:10],"...", PT[-10:])

#-- 암호문 만들기

CT = SubstLib.subst_encrypt(my_key, PT)

out_file = 'CIPHER-1_subst.txt'
   
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

'''

in_file = 'TEXT-1.txt'

if not os.path.exists(in_file):
    print("Working directory:", os.getcwd())
    print('File %s does not exist.' %(in_file))
    sys.exit()  # 프로그램 종료
    
#-- 입력파일에서 읽기
InFileObj = open(in_file)    
PT = InFileObj.read()
# 키가 랜덤하게 계속 바뀌기 때문에 위에꺼 주석 처리하고 고정
Key = 'VLXQRNZGKSPCWYDJUMAHBETFIO'
CT = SubstLib.subst_encrypt(Key, PT)

Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# 영문자 빈도순서
ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
def getItemAtIndexZero(items):
    return items[0]

def getLetterCount(message): 
    letterCount = {'A':0, 'B':0,'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0,'I':0,'J':0,
                   'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0,'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}

    for char in message.upper():
        if char in Alphabet:
            letterCount[char] += 1
    return letterCount


PT_count = getLetterCount(PT)
CT_count = getLetterCount(CT)

print(PT_count)
print(CT_count)


def getFreqOrder(message) :
    # - (letter, freq) 사전 만들기 : { 'A' : 999 , ....}
    letter2freq = getLetterCount(message)
    # - (freq, letter) 사전 만들기 : { 999 : ['A'], ... }
    freq2letter = {}
    for char in Alphabet:
        if letter2freq[char] not in freq2letter:
            freq2letter[letter2freq[char]] = [char]
        else :
            freq2letter[letter2freq[char]].append(char)
        
    for freq in freq2letter:
        freq2letter[freq].sort(key=ETAOIN.find, reverse=False)
        freq2letter[freq] = ''.join(freq2letter[freq])
        
    freqPairs = list(freq2letter.items())
    freqPairs.sort(key=getItemAtIndexZero, reverse=True)
    freqOrder = []
    for freq_pair in freqPairs:
        freqOrder.append(freq_pair[1])
    return ''.join(freqOrder)

PT_freq_str = getFreqOrder(PT)
CT_freq_str = getFreqOrder(CT)

print(PT_freq_str)
print(CT_freq_str)