#------------ README ----------------------------
'''

Install required libraries:
Windows: py -m pip install openpyxl matplotlib numpy
Unix/macOS: python -m pip install openpyxl matplotlib numpy
'''

import openpyxl
import matplotlib.pyplot as plt
import numpy as np
from math import log10, floor

# Load a file.
file = 'graph.xlsx'
wb = openpyxl.load_workbook(file)


#------------ READ ----------------------------
sheet1 = wb['Sheet1']

x = []
y = []
for i in range(1, sheet1.max_row + 1):
    
    # Read values at current row.
    xpoints = sheet1.cell(column=1, row=i).value
    ypoints = sheet1.cell(column=2, row=i).value
    
    # Append points to the lists.
    x.append(xpoints)
    y.append(ypoints)

#------------ WRITE ----------------------------
# Create Sheet2.
if 'Sheet2' not in wb.sheetnames:
    wb.create_sheet('Sheet2')
sheet2 = wb['Sheet2']

# Write to Sheet2.
for i in range(1, sheet1.max_row + 1):
    sheet2.cell(column=1, row=i).value = x[i - 1]
    sheet2.cell(column=2, row=i).value = y[i - 1]

wb.save(file)


#------------ DRAW ----------------------------

def round1(value):
    return round(value, -int(floor(log10(abs(value)))))


def roundPartial (value, resolution):
    if value > 0 and value < 1:
         decimal_places = len(str(value).split(".")[1])
         resolution = resolution * 10 ** -decimal_places
         
    return round (value /float(resolution)) * resolution
    
    

# Each point, calculates distance to line, returns average
def average_distance(slope):
    distances = []
    for i in range(len(x)):
        x_ = x[i]
        y_ = y[i]
        
        d = abs(slope * x_ - y_) / (1 + slope ** 2) ** (1/2)       
        distances += [d]
               
    return sum(distances) / len(distances)  



def slope():
    k = [0.0000001, 1, 100000]
    for o in range(50):
          
    # Calculate averages.
        a = []  
        for p in range(len(k)):       
            a += [average_distance(k[p])]
        
    # Numerical searching for optimal curve.
        m = a.index(min(a))
        if m == 0:
            k = [k[m], (k[m] + k[m + 1])/2, k[m + 1]]
            
        elif m == len(a) - 1:
            k = [k[m - 1], (k[m - 1] + k[m])/2, k[m]]
            
        else:   
            k = [k[m - 1],    (k[m - 1] + k[m])/2,    k[m],    (k[m] + k[m + 1])/2,    k[m + 1]]
    #            previous            avarage         current       avarage               next    
        
        if o == 49:
            return k[a.index(min(a))]
  
  
padding = 1.07
fig, ax = plt.subplots(2, 1)

############## PLOT 1 #################    
x = np.array(x)
y = np.array(y)

x2 = np.linspace(0, max(x) * padding, 1000)
y2 = 16704 * x2 ** -2

xspacing = round1(max(x) / 8)
yspacing = round1(max(y) / 6)
xspacing = roundPartial(xspacing, 5)
ax[0].set_xticks(np.arange(0, max(x) * padding, xspacing))
ax[0].set_xticks(np.arange(0, max(x) * padding, xspacing / 5), minor=True)
ax[0].set_yticks(np.arange(0, max(y) * padding, yspacing))
ax[0].set_yticks(np.arange(0, max(y) * padding, yspacing / 5), minor=True)
ax[0].spines['right'].set_color('#D7D7D7')
ax[0].spines['left'].set_visible(True)
ax[0].spines['top'].set_color('#D7D7D7')
ax[0].spines['bottom'].set_visible(True)
ax[0].grid(which='both')
ax[0].grid(which='minor', alpha=0.2)
ax[0].grid(which='major', alpha=0.5)


plt.subplot(2, 1, 1)
plt.plot(x, y, 'xk')
plt.plot(x2, y2, '-')

plt.xlim(0, max(x) * padding)
plt.ylim(0, max(y) * padding)
plt.tight_layout(pad=3)
plt.grid('both', 'both')
plt.title(label = r'$\bf{o(r)}$', pad = '20.0')
plt.xlabel(r'$r[cm]$', loc = 'right')
plt.ylabel('o[lux]', loc = 'top', rotation = 0) 
plt.legend(['Meritve', r'$y = k \cdot r^{-2}$'], loc = 'upper right')


############# PLOT 2 (linearizacija) #######
x = list(x)
for i in range(len(x)):
    x[i] = float(x[i]) ** -2
x = np.array(x)


x2 = np.linspace(0, max(x) * padding, 1000)
y2 = slope() * x2

xspacing = round1(max(x) / 8)
yspacing = round1(max(y) / 6)
xspacing = roundPartial(xspacing, 5)
ax[1].set_xticks(np.arange(0, max(x) * padding, xspacing))
ax[1].set_xticks(np.arange(0, max(x) * padding, xspacing / 5), minor=True)
ax[1].set_yticks(np.arange(0, max(y) * padding, yspacing))
ax[1].set_yticks(np.arange(0, max(y) * padding, yspacing / 5), minor=True)
ax[1].spines['right'].set_color('#D7D7D7')
ax[1].spines['left'].set_visible(True)
ax[1].spines['top'].set_color('#D7D7D7')
ax[1].spines['bottom'].set_visible(True)
ax[1].grid(which='both')
ax[1].grid(which='minor', alpha=0.2)
ax[1].grid(which='major', alpha=0.5)


plt.subplot(2, 1, 2)
plt.plot(x, y, 'xk')
plt.plot(x2, y2, '-')

plt.xlim(0, max(x) * padding)
plt.ylim(0, max(y) * padding)
plt.tight_layout(pad=3)
plt.grid('both', 'both')
plt.title(label = r'$\bf{o(r^{-2})}$', pad = '20.0')
plt.xlabel(r'$r^{-2}[cm]$', loc = 'right')
plt.ylabel('o[lux]', loc = 'top', rotation = 0) 
plt.legend(['Meritve', r'$y = k \cdot r$'], loc ='center right')

#plt.savefig("graf.png", dpi = 600, orientation = 'portrait', papertype = 'a4', format = 'png', bbox_inches = 'tight', pad_inches = 1, transparent = None)
#plt.savefig("graf.svg", dpi = 600, orientation = 'portrait', papertype = 'a4', format = 'svg', bbox_inches = 'tight', pad_inches = 1, transparent = None)
plt.show()

