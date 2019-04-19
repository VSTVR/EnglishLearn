import zipfile
import os

#把整个文件夹内的文件打包成zip文件（包括压缩路径下的字文件夹的文件）
def compress(get_files_path, set_files_path):
    f = zipfile.ZipFile(set_files_path , 'w', zipfile.ZIP_DEFLATED )
    for dirpath, dirnames, filenames in os.walk( get_files_path ):
        fpath = dirpath.replace(get_files_path,'') #注意2
        fpath = fpath and fpath + os.sep or ''     #注意2
        for filename in filenames:
            f.write(os.path.join(dirpath,filename), fpath+filename)
    f.close()
    print("压缩成功!!")


def backup():
    import time

    t = time.ctime().split()
    t_detail = t[3].split(':')
    filename = t[2] + '_' + t[1] + '_' + t[4] + ' ' + t_detail[0] + '时' + t_detail[1] + '分' + '.zip' #注意这里不能有:号，空格可以

    sourcepath = os.getcwd() + '/notebook'
    aimpath = os.getcwd() + '/backup/' + filename
    compress(sourcepath, aimpath)




#latest:



'''
    sourcepath = os.getcwd() + '/notebook'
    aimpath = os.getcwd() + '/backup/'  +'1.zip'
    compress(sourcepath, aimpath)
'''


'''
    sourcepath = os.getcwd() + '/' + 'notebook'
    aimpath = os.getcwd() + '/' + 'backup' +'/'+'1.zip'
    compress(sourcepath, aimpath)
'''
