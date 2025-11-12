import numpy as np

months= np.array(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
sales= []
print ("Enter the sales (in $1000) for each month")

for month in months:
  value= float(input(f"{month}: "))
  sales.append(value)

sales= np.array(sales)
print("\n ---- Company Sales Analysis---")
print("Total Sales of the Year:", np.sum(sales), "$")
print("Average Monthly Sales:", np.mean(sales), "$")
print("Highest Sales:", np.max(sales), "$")
print("Lowest Sales:", np.min(sales), "$")