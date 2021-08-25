
import xlrd, webbrowser

# Open a workbook.
workbook = xlrd.open_workbook(r'C:\Users\matey\Desktop\productCodes.xls')
sheet = workbook.sheet_by_index(0)

# Read the first column.
for row in range(sheet.nrows):
    code = int(sheet.cell_value(row, 0)
    link = 'https://www.qwant.com/?client=brz-brave&q=' + str(code) + '&t=web'
    webbrowser.open(link)
# Search for the code on a site.
