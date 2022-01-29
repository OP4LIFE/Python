import openpyxl
import matplotlib.pyplot as plt
import numpy as np

# Load koordinati.xlsx
wb = openpyxl.load_workbook('koordinati.xlsx')
sheet = wb['Sheet1']

xpoints = []
ypoints = []
for i in range(1, sheet.max_row + 1):
    
    # Read values at current row.
    x = sheet.cell(row=i, column=1).value
    y = sheet.cell(row=i, column=2).value
    
    # Apply the formula.
    x += 1
    y += 1
    
    # Append points to the lists.
    xpoints.append(x)
    ypoints.append(y)

# Convert lists to arrays.
xpoints = np.array(xpoints)
ypoints = np.array(ypoints)

# Draw points.
plt.plot(xpoints, ypoints, 'o-')
plt.show()
