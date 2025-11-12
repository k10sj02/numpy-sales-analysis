import numpy as np

months= np.array(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
sales= []
print ("Enter the sales (in $1000) for each month")

for month in months:
  value= float(input(f"{month}: "))
  sales.append(value)

sales= np.array(sales)