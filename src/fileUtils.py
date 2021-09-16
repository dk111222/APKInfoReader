
import sys
import tempfile
import subprocess
import os
import hashlib
import operator
import shutil


#解压缩apk包
# print("开始解压缩，第一个apk路径：{0}...".format(apk1))
# run_shell(u'{0} -y -o"{1}" x "{2}"'.format(z7, tempdir1, apk1))
# print("开始解压缩，第二个apk路径：{0}...".format(apk2))
# run_shell(u'{0} -y -o"{1}" x "{2}"'.format(z7, tempdir2, apk2))

#mayFreeze为false时，解压缩，为True时压缩
def run_shell(command, mayFreeze=False):
    def check_retcode(retcode, cmd):
        if 0 != retcode:
            print >> sys.stderr, 'err executing ' + cmd + ':', retcode
            sys.exit(retcode)
    def read_close(f):
        f.seek(0)
        d = f.read()
        f.close()
        return d
    #print >> sys.stderr, '-- Executing', command
    if mayFreeze:
        tempout, temperr = tempfile.TemporaryFile(), tempfile.TemporaryFile()#open(os.devnull, 'w')
        p = subprocess.Popen(command, stdout=tempout, stderr=temperr)
        p.wait()
        output, errout = read_close(tempout), read_close(temperr)
    else:
        p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = p.stdout.read()
        p.wait()
        errout = p.stderr.read()
        p.stdout.close()
        p.stderr.close()
    #check_retcode(p.returncode, command)
    return (output.strip(), errout.strip())


#删除一个文件夹下所有的文件
def del_allfile(path):
    list = os.listdir(path)
    for i in range(0,len(list)):
        singlepath = os.path.join(path,list[i])
        # print(singlepath)
        if(os.path.isfile(singlepath)):
            os.remove(singlepath)
        else:
            del_allfile(singlepath)
    return

#删除一个文件夹下所有的文件夹
def del_alldir(path):
    list = os.listdir(path)
    # print(path)
    # if(len(list) == 0):
    #     os.rmdir(path)
    #     return
    for i in range(0,len(list)):
        singlepath = os.path.join(path,list[i])
        # print(singlepath)
        del_alldir(singlepath)
        os.rmdir(singlepath)
    return
