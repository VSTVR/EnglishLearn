# coding=utf-8

import os
def semicolon_exist(word):
    if ';'in word:
        return True
    elif '；'in word:
        return True
    else:
        return False

def split(word):
    if ';'in word:
        return word.split(';')
    elif '；'in word:
        return word.split('；')
    else:
        return word.split()

def isinessentialword(word,lists):
    for l in lists:
        if word in l:
            return True
    return False

def isin(word,lists):
    for l in lists:
        if word in l:
            return l,True
    return None,False
def getcontent(path):
    list=[]
    fp=open(path,'r')
    list=fp.readlines()
    fp.close()
    return list

def main():
    path=os.getcwd()+'/notebook/'+'word.txt'
    extrapath=os.getcwd()+'/notebook/'+'essentialword.txt'
    helppath=os.getcwd()+'/'+'helpdoc.txt'

    while 1:
        word = input('请输入想要记录的单词(第一次使用请输入#help开启帮助文档)：')
        wordcut = split(word)
        lists = getcontent(path)
        extralist=getcontent(extrapath)
        aim ,boolresult=isin(wordcut[0],lists)

        if semicolon_exist(word)is True:
            if boolresult is True:
                print('已存在:', aim)
                if isinessentialword(wordcut[0], extralist) is False:
                    fp = open(extrapath, 'a')
                    fp.write(aim + '\n')
                    fp.close()
            else:
                fi = open(path, 'a')
                fi.write(wordcut[0] + '——' + wordcut[1] + '\n')
                fi.close()

        elif '#'in word:
            if word=='#help':
                f = open(helppath, 'rt')
                data = f.read()
                f.close()
                print(data)

            elif word=='#backup':
                from createzip import backup
                backup()

        elif semicolon_exist(word)is False:
            if boolresult is True:
                print('存在：',aim)
            else:
                print('不存在')





if __name__ == '__main__':
    main()
