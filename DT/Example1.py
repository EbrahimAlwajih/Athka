from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
import pandas as pd

# Sample data
data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Overcast'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal'],
    'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong'],
    'PlayTennis': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes']
}

df = pd.DataFrame(data)

# Preprocessing: Convert string labels into numbers
labelEncoder = preprocessing.LabelEncoder()
for col in df.columns:
    df[col] = labelEncoder.fit_transform(df[col])

# Feature set and target variable
X = df.drop('PlayTennis', axis=1)
y = df['PlayTennis']

# Create a decision tree classifier
clf = DecisionTreeClassifier()
clf = clf.fit(X, y)

# Predict for a new set of data
prediction = clf.predict([[0, 2, 0, 1]])  # Example: ['Sunny', 'Cool', 'High', 'Strong']
print("Predicted class:", labelEncoder.inverse_transform(prediction)[0])
