import xlrd

# 打开excel
book = xlrd.open_workbook('../data/data1.xls')
# 定位sheet表
table = book.sheet_by_name('Sheet1')
# 获取数据
print(table.nrows) #获取行数
print(table.ncols) #获取列数
print(table.col_values(1)) #获取第二列的数据
print(table.row_values(2)) #获取第三行的数据