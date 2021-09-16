# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
from src import adbUtils, excelUtils
from src.APK import APKInfo

import xlrd, xlwt, xlutils.copy, xlutils

# build EXE Command：
# pyinstaller -D main.py -p src\excelUtils.py -p src\adbUtils.py -p src\APK.py -p src\fileUtils.py
#
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('== pkgInfo.xls 路径： %s  ===' )

    print('- 1. 前置：填好 pkgInfo.xls， 并存储在路径下： %s' % adbUtils.APK_CHECKER_PATH)
    print('          已配置Android adb等环境变量(adb, aapt, keytool) ')
    print('          将相关apk存储在%s并解压， 或将手机连接PC' % adbUtils.APK_CHECKER_PATH)
    print('- 2. 执行脚本，读取需要解析的应用信息 ')
    pkgNames = excelUtils.readPkgInfos()

    for pkgName in pkgNames:
        # pkgName是字符串并且以com.开头的包名
        if isinstance(pkgName, str) and pkgName.startswith('com.'):
            try:
               adbUtils.pullApkToCheckerPath(pkgName)
            except Exception as e:
                print("     未找到%s的APK：, Exception: %s " % (pkgName, str(e)))

    input("- 3. %s目录中APK解压完成后，回车继续！" % adbUtils.APK_CHECKER_PATH)

    for pkgName in pkgNames:
        # pkgName是字符串并且以com.开头的包名
        if isinstance(pkgName, str) and pkgName.startswith('com.'):
            apkInfo = APKInfo(pkgName)
            try :
                apkInfo.parse()
                # apkInfo.dump()
                excelUtils.saveApkInfo(apkInfo)
            except Exception as e:
                print("     %s parse Exception %s" %(pkgName, str(e)))

    print('- 4. 提取信息结束，请检查： pkgInfo.xls 中信息')

    os.system("pause")

# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
