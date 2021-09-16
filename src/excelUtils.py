# import pandas as pd

# 读, 写, 改表格
# https://www.cnblogs.com/yunguoxiaoqiao/p/7592000.html
import xlrd   #Xlrd模块只能用来读取数据操作，无法修改数据。
import xlwt
from xlutils.copy import copy   #导入copy模块

from src.adbUtils import APK_CHECKER_PATH

PKG_INFO_FILE = r'%s\pkgInfo.xls'%APK_CHECKER_PATH

COLUMNS_NAME = ""


def readExcelExample():
    data = xlrd.open_workbook(PKG_INFO_FILE)  # 打开.xlsx文件读取数据, need: pip install pyexcel-xls
    table = data.sheets()[0]  # 读取第一个（0）表单
    # 或者通过表单名称获取 table = data.sheet_by_name(u'Sheet1')

    print(table.nrows)  # 输出表格行数
    print(table.ncols)  # 输出表格列数
    print("第一行：", table.row_values(0))  # 输出第一行
    print("第一列：", table.col_values(0))  # 输出第一列
    print("第一行第3列：", table.cell(0, 2).value)  # 输出元素（0,2）的值

def writeExcelExample():
    wb = xlwt.Workbook(encoding='ascii')  # 创建新的Excel（新的workbook），建议还是用ascii编码
    ws = wb.add_sheet('weng')  # 创建新的表单weng
    ws.write(0, 0, label='hello')  # 在（0,0）加入hello
    ws.write(0, 1, label='world')  # 在（0,1）加入world
    ws.write(1, 0, label='你好')
    wb.save('weng.xls')  # 保存为weng.xls文件

def editExcelExample():
    rb = xlrd.open_workbook(PKG_INFO_FILE)  # 打开weng.xls文件
    wb = copy(rb)  # 利用xlutils.copy下的copy函数复制
    ws = wb.get_sheet(0)  # 获取表单0
    ws.write(8, 0, label='好的')  # 增加（8,0）的值
    wb.save(PKG_INFO_FILE)  # 保存文件

def saveApkInfo(apkInfo):
    rb = xlrd.open_workbook(PKG_INFO_FILE)  # 打开weng.xls文件
    table = rb.sheets()[0]  # 读取第一个（0）表单
    i = 1
    while (i < table.nrows) :
        if table.cell(i, 0).value == apkInfo.pkgName:
            wb = copy(rb)  # 利用xlutils.copy下的copy函数复制
            ws = wb.get_sheet(0)  # 获取表单0
            if (table.ncols >3) :
                ws.write(i, table.ncols - 2, label=apkInfo.apkVersionInfo)  # 增加（8,0）的值
                ws.write(i, table.ncols - 1, label=apkInfo.apkSignerInfo)  # 增加（8,0）的值
            else :
                ws.write(i, 3, label=apkInfo.apkVersionInfo)  # 增加（8,0）的值
                ws.write(i, 4, label=apkInfo.apkSignerInfo)  # 增加（8,0）的值
            wb.save(PKG_INFO_FILE)  # 保存文件
            return
        i += 1

def readPkgInfos () :
    # read_excel()用来读取excel文件，记得加文件后缀
    data = xlrd.open_workbook(PKG_INFO_FILE)  # 打开.xlsx文件读取数据, need: pip install pyexcel-xls
    table = data.sheets()[0]  # 读取第一个（0）表单
    return table.col_values(0)
    # sheet_name = r'包名'
    # sheet_data = pd.read_excel(PKG_INFO_FILE, sheet_name=sheet_name)
    # print(sheet_data)

    # print('显示表格的属性:', data.shape[0])  # 打印显示表格的属性，几行几列
    # print('显示表格的列名:', data.columns)  # 打印显示表格有哪些列名
    # # head() 默认显示前5行，可在括号内填写要显示的条数
    # print('显示表格前3行:', data.head(2))
    # print('----------华丽的分割线 -----------')
    # # tail() 默认显示后5行，可在括号内填写要显示的条数
    # print('显示表格后五行:', data.tail(2))



def toExcel (pkgNames) :
    print("toExcel")
    # # nan_excle = pd.DataFrame()
    # # nan_excle.to_excel(PKG_INFO_FILE2)
    # data = pd.read_excel(PKG_INFO_FILE)
    # excel = pd.DataFrame(data).to_excel()
    # writer = pd.ExcelWriter()
    #
    # # # 打开excel
    # # writer = pd.ExcelWriter(PKG_INFO_FILE)
    # # # sheets是要写入的excel工作簿名称列表
    # for sheet in writer.sheets:
    #     # 保存writer中的数据至excel
    #     # 如果省略该语句，则数据不会写入到上边创建的excel文件中
    # writer.save()