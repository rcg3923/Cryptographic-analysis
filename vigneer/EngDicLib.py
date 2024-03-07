#--------------------------
# 암호분석 - 영어사전 라이브러
#--------------------------

#-- 특수문자를 지우기 위한 상수
UpAlphabet    = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters_and_space = UpAlphabet + UpAlphabet.lower() + ' \t\n'

#-- 영어사전 파일 읽기
def loadDic():
    dictionary_file = open('EngDic.txt')
    EnglishWords = {}
    # 파일을 읽어(read()), 리스트로 나눈다(split())
    for word in dictionary_file.read().split('\n'):
        # EnglishWords[word] = None
        EnglishWords[word] = len(word)
    dictionary_file.close()
    return EnglishWords

# 사전 변수 - 전역변수에 사전파일을 읽어둔다.
EnglishWords = loadDic()
#print('The number of words is', len(EnglishWords))
#print(EnglishWords['zoo'])

#-- IC: Index of Coincidence
def IC(msg):
    AlphaDic = {}
    for ch in UpAlphabet:
        AlphaDic[ch] = 0
        
    num_alpha = 0
    for ch in msg:
        if ch.upper() in UpAlphabet: 
            AlphaDic[ch.upper()] += 1
            num_alpha += 1
    
    ic = 0
    for ch in UpAlphabet:
        ic += AlphaDic[ch]*(AlphaDic[ch]-1)
    ic /= num_alpha*(num_alpha-1)
    return ic

# 대소문자, 공백, 탭, 리턴만 남긴다
def removeNonLetters(message):
    letters_only = []
    for ch in message:
        if ch in letters_and_space:
            letters_only.append(ch)
    return ''.join(letters_only)

#---- 올바른 영어단어의 비율
def percentEnglishWords(message):
    message = message.lower()
    message = removeNonLetters(message)
    possible_words = message.split()
    #print(possible_words)  # 확인용 #--> ['my', 'name', 'is', 'yongjin', 'yeom']
    
    if possible_words == []:
        return 0.0
    count_words = 0
    for word in possible_words:
        if word in EnglishWords:
            count_words += 1
    return float(count_words)/len(possible_words) 

#-- 영어인지 판정하는 함수
def isEnglish(message, wordPercentage=20, letterPercentage=80):
        wordsMatch = percentEnglishWords(message)*100 >= wordPercentage        
        numLetters = len(removeNonLetters(message))
        messageLettersPercentage = float(numLetters) / len(message) * 100
        lettersMatch = messageLettersPercentage >= letterPercentage      
        return wordsMatch and lettersMatch
 
#-- 알파벳 빈도를 사전으로 만들기
def LetterFreq(msg):
    lfDic = {}
    for ch in UpAlphabet:
        lfDic[ch] = 0
    for ch in msg.upper():
        if ch in UpAlphabet:
            lfDic[ch] += 1
    return lfDic

#-- 빈도별 알파벳을 사전으로 만들기 (LetterFreq를 반대로)
def FreqLetter(lfDic):
    flDic = {}
    for ch in UpAlphabet:
        if lfDic[ch] not in flDic:
            flDic[lfDic[ch]] = [ch]
        else:
            flDic[lfDic[ch]].append(ch)
    
    return flDic
    
#=== 라이브러리 동작확인을 위한 함수 
def main():
    print("EngDicLib test...")
    
    msg = 'My name is Yongjin Yeom.'
    #print(percentEnglishWords(msg)) #--> 0.2
    
    msg1 = "What is Caesar cipher? Is it secure?"
    msg2 = "Zkdw lv Fdhvdu flskhu? Lv lw vhfxuh?"
    
    print('msg1 = ', msg1[:30],'...')
    print('msg2 = ', msg2[:30],'...')
    print('msg1 is English:', isEnglish(msg1))
    print('msg2 is English:', isEnglish(msg2))

    print('Index of Coincidence, IC(msg) = %6.4f' %(IC(msg)))
    print('Index of Coincidence, IC(msg1) = %6.4f' %(IC(msg1)))
    print('Index of Coincidence, IC(msg2) = %6.4f' %(IC(msg2)))
    
    freq_letter = LetterFreq(msg)
    letter_freq = FreqLetter(freq_letter)
    print(freq_letter)
    print(letter_freq)
    
#========
if __name__ == '__main__':
    main()
    
# main() 실행결과
'''    
EngDicLib test...
msg1 =  What is Caesar cipher? Is it s ...
msg1 =  Zkdw lv Fdhvdu flskhu? Lv lw v ...
msg1 is English: True
msg2 is English: False
'''