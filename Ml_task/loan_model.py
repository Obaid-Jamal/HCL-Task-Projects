import numpy as np
from sklearn.tree import DecisionTreeClassifier

# Training data
X = np.array([
    [20000, 600],
    [30000, 650],
    [40000, 700],
    [50000, 750]
])

y = np.array([0, 0, 1, 1])

# Model
model = DecisionTreeClassifier()
model.fit(X, y)

def check_loan(income, credit):
    return model.predict([[income, credit]])[0]