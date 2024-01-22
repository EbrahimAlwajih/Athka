import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

study_hours = np.array([2, 3, 4, 5, 6, 7, 8, 9])
sleep_hours = np.array([6, 7, 5, 8, 7, 7, 8, 6])
test_scores = np.array([75, 80, 85, 90, 95, 90, 95, 90])

X = np.column_stack((study_hours, sleep_hours))
print(X.shape)
model = LinearRegression()
model.fit(X, test_scores)
predicted_scores = model.predict(X)

for actual, predicted, study, sleep in zip(test_scores, predicted_scores, study_hours, sleep_hours):
    print(f"Study: {study} hrs, Sleep: {sleep} hrs, Actual Score: {actual}, Predicted Score: {round(predicted, 2)}")

Test = model.predict( np.array([[6.5, 8],[10,10]]))
print(Test)