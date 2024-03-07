"""
    
    python practice 2
    
    
"""
    
# 파일 입출력
'''

라이브러리 : os, sys

os.getcwd(),  os.chdir(), os.path.exists(), sys.exit()
파일 : open(), close(), read(), write()

'''

import os, sys

'''
# 작업 폴더
print('current working directory = ',os.getcwd() )
os.chdir('/Users/kch/Desktop/암호분석/')
print('current working directory = ',os.getcwd() )

in_file = 'PT1.txt'
if not os.path.exists(in_file):
    print('File not found error.')
    sys.exit()
    
infile_object = open(in_file)
my_contents = infile_object.read()
print(my_contents[:20], '...', my_contents[-20:])
infile_object.close()


out_file = 'OUT1.txt'
if os.path.exists(out_file):
    print("Really overwirte? (Y/N) > ")
    response = input()
    if not (response == 'Y'):
        sys.exit()
        
outfile_object = open(out_file, 'w')
outfile_object.write(my_contents)
outfile_object.close()

'''

# List - (서로 다른) 데이터의 모임 (순서쌍) 
# Example : list1 = [0, 3.14, 'hi']

animals = ['cat', 'dog', 'lion', 'tiger']
print(animals)

animals.append('snake')
# animals += ['man', 'woman']
# animals += 'man'
# animals += list('woman')
print(animals)

for i in animals:
    print('I want to have a', i)
    
#join() 함수
str1 = ''

new_str1 = str1.join(animals)
print(new_str1)

    
# Dictionary


