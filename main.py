import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Create an array
x = np.arange(10)
y = np.random.randint(low=1, high=10, size=10)

# Preprocessing Input data
data = pd.read_csv(r'C:\Users\asadm\OneDrive\Рабочий стол\mnk\pearson.csv')
x = data['Father'].values
y = data['Son'].values

n = len(x)

u1 =  np.ones(n)
A = np.concatenate([u1, x], axis = 0)
A = np.reshape(A, [n, 2], order = 'F')

B = np.matmul(A.T, A)
B = np.linalg.inv(B)

A = np.matmul(B, A.T)
u = np.matmul(A, y)

y_est = u[0] + u[1]*x

plt.scatter(x, y, color = 'red')
plt.plot([min(x), max(x)], [min(y_est), max(y_est)], color = 'blue')
plt.xlabel('Fathers height')
plt.ylabel('Sons height')
plt.show()