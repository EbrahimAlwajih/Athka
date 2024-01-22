import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Simple Linear Regression: Predicting Grades based on Study Hours
study_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
grades = np.array([50, 55, 60, 65, 70, 75, 80, 85])

model = LinearRegression()
model.fit(study_hours, grades)
predicted_grades = model.predict(study_hours)

plt.scatter(study_hours, grades, color='green', label='Actual Grades')
plt.plot(study_hours, predicted_grades, color='orange', label='Predicted Line')
plt.title('Study Hours vs Grades')
plt.xlabel('Hours of Study')
plt.ylabel('Grades')
plt.legend()
plt.show()
Test = model.predict( np.array([20, 2.5]).reshape(-1, 1))
print(Test)