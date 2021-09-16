from src import adbUtils

class APKInfo:
    pkgName = None
    pathInDevice = None #手机中存储路径

    apkName = None

    apkVersionInfo = None  # 版本号， 版本名字等

    apkSignerInfo = None # 签名信息

    def __init__(self, pkgName):
        self.pkgName = pkgName
        self.pathInDevice = adbUtils.getPkgPathFromDevice(self.pkgName)
        # 读取APK名字
        paths = self.pathInDevice.split("/")
        self.apkName = paths[len(paths) - 2]

    def parse(self):
        # 本地存储的路径
        print("正在解析: %s " % self.pkgName)
        apkLocalPath = adbUtils.APK_CHECKER_PATH + '/' + self.apkName + ".apk"
        # 读取APK版本号
        self.apkVersionInfo = adbUtils.getApkVersionInfo(apkLocalPath)

        # 从解压的CERT.RSA中读取签名信息
        self.apkSignerInfo = adbUtils.getApkSignerInfo(self.apkName)


    def dump(self):
        dumpInfo = "-------------------\npkgName: %s, apkName: %s\napkVersionInfo: %s \napkSignerInfo: %s"% (self.pkgName, self.apkName, self.apkVersionInfo, self.apkSignerInfo)
        print(dumpInfo)

