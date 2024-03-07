'''

암호분석 - english dictionary library

'''
import os
import sys
# 영어 대문자
UpAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# 영어 대소문자, 공백, 탭, 엔터
letters_and_space = UpAlphabet + UpAlphabet.lower() + ' \t\n' 

#=== dictionary data type (key, value) example : (apple, 사과)
'''
myDic = { 'DES': 64, 'AES' : 128 }
print(myDic)
print(myDic['DES'])
myDic['ARIA'] = 128
print(myDic)

'''


#-- Reading the  English Dictonary file --> dictionary 변수 만들기

def loadDic():
    dic_file = open('EngDic.txt')
    # Not found file -> error..
    EngWords = {} # empty dictionary
    contents = dic_file.read()
    #split 이 뭔지 알아보자
    contents_list = contents.split('\n')
    for word in contents_list:
        #EngWords[word]
        EngWords[word] = len(word)
    dic_file.close()
    return EngWords

# 영어 사전 변수 전역변수로 생성
EnglishDic = loadDic()

# 대소문자, 공백, 탭, 리턴만 남기기
def removeNoneLetters(msg):
    letters_list = []
    for ch in msg:
        if ch in letters_and_space:
            letters_list.append(ch)
    return ''.join(letters_list) # 리스트를 문자열로 


# 복호화한 문서에서 영어단어의 비율
def percentEngWords(msg):
    msg = msg.lower() #msg를 소문자로 만든다
    msg = removeNoneLetters(msg) #특수문자, 숫자 지움
    possible_words = msg.split() # 문자열을 리스트로 
    if possible_words == []: #0으로 나누기 방지
        return 0.0
    count_words = 0
    for word in possible_words:
        if word in EnglishDic: #사전에 있는 단어인가?
            count_words += 1
    return float(count_words) / len(possible_words)


# 영어인지 판정하기
def isEnglish(msg, wordPercentage = 20, letterPercentage = 80):
    wordMatch = percentEngWords(msg)*100 >= wordPercentage
    numLetters = len(removeNoneLetters(msg))
    messageLetters_Percentage = float(numLetters)*100/len(msg)
    
    letterMatch = messageLetters_Percentage >= letterPercentage
    
    return wordMatch and letterMatch

# IC : Index of Coincidence
def IC(msg):
    AlphaDic = {}
    for ch in UpAlphabet:
        AlphaDic[ch] = 0
    num_Alpha = 0
    for ch in msg:
        if ch.upper() in UpAlphabet:
            AlphaDic[ch.upper()] += 1
            num_Alpha += 1
    ic = 0
    for ch in UpAlphabet:
        ic += AlphaDic[ch] * (AlphaDic[ch]-1)
    ic /= num_Alpha*(num_Alpha-1)
    return ic
    
def main():
    # msg1이 맞는지 판단하기.
    msg1 = 'Caesar cipher is not secure.'
    print('msg1 = ', msg1)
    print('English Percent: ', percentEngWords(msg1))
    print('msg is English :', isEnglish(msg1))
    print('msg1: index of conincidence = ', IC(msg1))
if __name__ == '__main__':
    main()

