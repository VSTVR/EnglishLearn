import os
def ishadfuhao(word):
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
def getall(path):
    list=[]
    fp=open(path,'r')
    list=fp.readlines()
    fp.close()
    return list

def main():
    path=os.getcwd()+'/'+'word.txt'
    extrapath=os.getcwd()+'/'+'essentialword.txt'

    while 1:
        word = input('请输入想要记录的单词(以“;”为中英文分界)：')
        wordcut = split(word)
        lists = getall(path)
        extralist=getall(extrapath)
        aim ,boolresult=isin(wordcut[0],lists)

        if ishadfuhao(word)is True:
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
        elif ishadfuhao(word)is False:
            if boolresult is True:
                print('存在：',aim)
            else:
                print('不存在')