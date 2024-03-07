
# -*- coding: utf-8 -*-
#-----------------------------
# 암호분석 - Shallow/Deep copy, random
#-----------------------------

#== [1] 깊은 복사, 얕은 복사
'''
list1 = ['a', 'b', 'c', 'd']
print(list1, id(list1))
list2 = list1
print(list2, id(list2))
list2.append('e')
print(list1, id(list1))
print(list2, id(list2))


import copy # library for deep copy
list3 = copy.deepcopy(list1)
print(list1, id(list1))
print(list3, id(list3))
list3.append('f')
print(list1, id(list1))
print(list3, id(list3))
'''


# using Slice operator to copy

# shallow copy --- deep copy


# == [2] 정렬(sort) - selection, bubble, insertion, merge, q
'''

# 이 부분 영상으로 복습
list4 = list('Fuck!')
print(list4)
list4.sort(key=UpAlphabet.find, reverse=True)
# key=ftn 함수 이름 : ftn 함수를 호출하여 크기를 비교

print(list4)
#영어 대문자
UpAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

'''




#== [3] 난수 만들기, 섞기
import random
import time
import copy

# (의사)난수만드는 방법 = pseudo-random number generation
# 입력 : seed --- [복잡한 알고리즘] ---> 난수 (통계적으로 랜덤)

random.seed(time.time())
print(random.randint(1, 6)) # 1,2,3,4,5,6 중에 무작위
print(random.randint(1, 6)) 
print(random.randint(1, 6)) 

# shuffling

UpAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

alpha_list = list(UpAlphabet)

print(UpAlphabet)
print(alpha_list)
random.shuffle(alpha_list)
print(alpha_list)
shuffled = ''.join(alpha_list)
print(shuffled)

sorted_list = alpha_list #shallow copy

sorted_list = copy.deepcopy(alpha_list)
sorted_list.sort(key = UpAlphabet.find)
print('before_sort', alpha_list)
print('after_srot', sorted_list)
sorted = ''.join(sorted_list)
print(shuffled)
print(sorted)

