'''

'''
import sys, os
import caesar_lib as Caesar



'''
in_file = 'PT1.txt'
if not os.path.exists(in_file):
    print('File not found error.')
    sys.exit()
    
infile_object = open(in_file)
my_contents = infile_object.read()
print(my_contents[:20], '...', my_contents[-20:])
infile_object.close()

'''

'''

# Caesar 암호화
key = 3
CT = Caesar.Caesar_Enc(key, my_contents)

out_file = 'CT1.txt'
if os.path.exists(out_file):
    print("Really overwirte? (Y/N) > ")
    response = input()
    if not (response == 'Y'):
        sys.exit()
        
outfile_object = open(out_file, 'w')
outfile_object.write(CT)
outfile_object.close()


# Caesar 복호화

recPT = Caesar.Caesar_Dec(key, CT)

out_file = 'recPT1.txt'
if os.path.exists(out_file):
    print("Really overwirte? (Y/N) > ")
    response = input()
    if not (response == 'Y'):
        sys.exit()
        
outfile_object = open(out_file, 'w')
outfile_object.write(recPT)
outfile_object.close()

'''

'''

Caesar 암호화 / 복호화
Caesar 암호해독 방법
    (1) key = 0, 1, 2, 3 ..., 25 전수조사 해보기
    (2) 올바른 키를 찾았는지 판단은? --> 자동화

'''

import english_dictionary_lib


in_file = 'CT1.txt'
if not os.path.exists(in_file):
    print('File not found error.')
    sys.exit()
    
infile_object = open(in_file)
my_contents = infile_object.read()
print(my_contents[:20], '...', my_contents[-20:])
infile_object.close()

for Key in range(0,26): # 0,1 ,..... ,25
    decodedPT = Caesar.Caesar_Dec(Key, my_contents)
    if english_dictionary_lib.isEnglish(decodedPT):
        print('Right Key = ', Key)
        print(decodedPT[:20], '...', decodedPT[-20:])
        
    # print('key = ', key, end ='')
    # print(decodedPT[:20], '...', decodedPT[-20:])
    
