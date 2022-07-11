import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# preprocessing Input data
data = pd.read_csv(r'C:\Users\asadm\OneDrive\Рабочий стол\mnk\pearson.csv')
X = data['Father'].values
Y = data['Son'].values

# calculate mean of x & y using an inbuilt numpy method mean()
mean_x = np.mean(X)
mean_y = np.mean(Y)

# total № of input values
m = len(X)

# using the formula to calculate a & b
numer = 0
denom = 0
for i in range(m):
  numer += (X[i] - mean_x) * (Y[i] - mean_y)
  denom += (X[i] - mean_x) ** 2
a = numer / denom
b = mean_y - (a * mean_x)

print (f'a = {a} \nb = {b}')

# plotting values and regression line
max_x = np.max(X) + 10
min_x = np.min(Y) - 10

# calculating line values x and y
x = np.linspace (min_x, max_x, 100)
y = b + a * x

plt.plot(x, y, color='blue', label='Regression Line')
plt.scatter(X, Y, c='red', label='data points')

plt.xlabel('Fathers height')
plt.ylabel('Sons height')
plt.legend()
plt.show()
