import numpy as np
from sklearn.linear_model import LinearRegression

# Training data
X = np.array([[1],[2],[3],[4],[5]])
y = np.array([20000,30000,40000,50000,60000])

# Model
model = LinearRegression()
model.fit(X, y)

def predict_salary(exp):
    return model.predict([[exp]])[0]