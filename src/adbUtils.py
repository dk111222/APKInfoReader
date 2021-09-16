import os, re

APK_CHECKER_PATH = r'D:\apkChecker'

AAPT_PATH = r'C:\Users\gree\AppData\Local\Android\Sdk\build-tools\30.0.3\aapt'

def runAdbCmd(cmd) :
    os.open(cmd)

def runCmdForResult(cmd):
    return os.popen(cmd)

def shortCutScreen():
    os.system("adb shell /system/bin/screencap -p /sdcard/screen.png")  # 截取屏幕，图片命名为screen.png

def pullApkToCheckerPath(pkgName):
    pathInDevice = getPkgPathFromDevice(pkgName)
    # 读取APK名字
    paths = pathInDevice.split("/")
    apkName = paths[len(paths) - 1]
    apkLocalPath = r'%s\%s'%(APK_CHECKER_PATH, apkName)
    if (os.path.isfile(apkLocalPath)) :
        print("     %s already exist! " % apkLocalPath)
        return

    os.system("adb pull %s  %s " % (pathInDevice, APK_CHECKER_PATH))


#从手机设备中读取apk路径
def getPkgPathFromDevice(pkgName):
    return os.popen("adb shell pm -p %s" % pkgName).read().split(":")[1].replace("\t", "").replace("\n", "")

#从手机设备中读取安装的应用包名信息
def getPkgNamesFromDevice() :
    pkgList = os.popen("adb shell pm list packages").read().split("\n");
    pkgNames = []
    for pkg in pkgList:
        if (len(pkg) > 10) :
            pkgNames.append(pkg.split(":")[1])
    return pkgNames

# 读取apk基本信息
def getApkVersionInfo(apkPath):
    #检查版本号等信息
    # output = os.popen("aapt d badging %s" % apkPath).read()
    # output = os.popen(r'aapt d badging D:\apkChecker\GreeSystemUI.apk').read().decode()
    with os.popen("aapt d badging %s" % apkPath) as fp:
        output = fp._stream.buffer.read().decode().strip()
        # package: name = 'com.android.systemui' versionCode = '32' versionName = '1.0.30_210907'
        info = re.compile(r"package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'").match(output)
        # packageName = info.group(1)
        # versionCode = info.group(2)
        # versionName = info.group(3)

        return '版本号：' + info.group(2) + ' 版本：' + info.group(3)

def getApkSignerInfo(apkName):
    # keytool -printcert -file "C:\Users\xxx\Desktop\CERT.RSA"
    # CERT.RSA：解压APK，将其中META-INF文件夹解压出来，得到其中的CERT.RSA文件
    # GET_SIGNER_CMD = r'keytool -printcert -file  D:\apkChecker\GreeSystemUI\META-INF\CERT.RSA'
    CERT_PATH = r'%s\%s\META-INF\CERT.RSA' %(APK_CHECKER_PATH, apkName)

    if (os.path.isfile(CERT_PATH) is False) :
        print("     没有找到%s,请先解压apk" % CERT_PATH)

    with os.popen(r'keytool -printcert -file  D:\apkChecker\%s\META-INF\CERT.RSA' %apkName) as fp:
        output = fp.read()
        infos = output.split('\n')
        if (len(infos) > 9) :
            return '%s\n%s\n%s\n%s\n%s'%(str(infos[4]),str(infos[5]), str(infos[6]), str(infos[7]), str(infos[8]))
        return output