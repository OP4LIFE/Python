
import xlrd

# Open a workbxook.
workbook = xlrd.open_workbook("Path to the file")
sheet = workbook.sheet_by_index(0)

# Read first column manually.
print(sheet.cell_value(0, 0))
print(sheet.cell_value(0, 1))
print(sheet.cell_value(0, 2))
print(sheet.cell_value(0, 3))


