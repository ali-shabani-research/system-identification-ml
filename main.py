import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 1: Simulate a dynamical system
T = 100
a = 0.8
x = [1]

for t in range(T):
    x.append(a * x[-1] + 0.2 * x[-1]**2 + np.random.normal(0, 0.1))

# Step 2: Prepare data for learning
X = np.array(x[:-1]).reshape(-1, 1)
y = np.array(x[1:])

# Step 3: Learn system dynamics
model = LinearRegression()
model.fit(X, y)

print("True coefficient:", a)
print("Learned coefficient:", model.coef_[0])

# Step 4: Plot results
plt.plot(x, label="System Output")
plt.title("Simulated Dynamical System")
plt.legend()
plt.show()
