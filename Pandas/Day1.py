import numpy as np
import pandas as pd

data = pd.read_csv(r"C:\Users\VICKY\OneDrive\Desktop\Sourcesys\Pandas\Titanic-Dataset.csv")

print("First 10 Rows")
print(data.head(10))

print("\nLast 10 Rows")
print(data.tail(10))

print("\nShape of Dataset")
print(data.shape)

print("\nColumn Names")
print(data.columns)

print("\nDataset Information")
print(data.info())

print("\nStatistical Summary")
print(data.describe())

print("\nMissing Values")
print(data.isnull().sum())

data["Age"].fillna(data["Age"].mean(), inplace=True)
data["Embarked"].fillna(data["Embarked"].mode()[0], inplace=True)

print("\nMissing Values After Cleaning")
print(data.isnull().sum())

print("\nPassenger Age Column")
print(data["Age"])

print("\nPassengers older than 40")
print(data[data["Age"] > 40])

print("\nPassengers in First Class")
print(data[data["Pclass"] == 1])

print("\nAverage Age by Gender")
print(data.groupby("Sex")["Age"].mean())

print("\nAverage Fare by Passenger Class")
print(data.groupby("Pclass")["Fare"].mean())

print("\nSurvival Count by Gender")
print(data.groupby("Sex")["Survived"].sum())

print("\nSorting by Age")
print(data.sort_values(by="Age").head())

print("\nSorting by Fare")
print(data.sort_values(by="Fare", ascending=False).head())

data["Fare_Per_Age"] = data["Fare"] / data["Age"]

print("\nNew Column Added")
print(data[["Fare", "Age", "Fare_Per_Age"]].head())

age_array = np.array(data["Age"])
fare_array = np.array(data["Fare"])

print("\nNumPy Age Array")
print(age_array)

print("\nNumPy Fare Array")
print(fare_array)

print("\nAverage Age")
print(np.mean(age_array))

print("\nMaximum Age")
print(np.max(age_array))

print("\nMinimum Age")
print(np.min(age_array))

print("\nStandard Deviation of Age")
print(np.std(age_array))

print("\nAverage Fare")
print(np.mean(fare_array))

print("\nMaximum Fare")
print(np.max(fare_array))

print("\nMinimum Fare")
print(np.min(fare_array))

print("\nStandard Deviation of Fare")
print(np.std(fare_array))

print("\nCorrelation Matrix")
print(data.corr(numeric_only=True))

matrix1 = np.array([[2,4,6],
                    [1,3,5],
                    [7,9,11]])

matrix2 = np.array([[1,0,2],
                    [3,1,4],
                    [5,2,6]])

print("\nMatrix 1")
print(matrix1)

print("\nMatrix 2")
print(matrix2)

print("\nMatrix Addition")
print(np.add(matrix1, matrix2))

print("\nMatrix Subtraction")
print(np.subtract(matrix1, matrix2))

print("\nMatrix Multiplication")
print(np.dot(matrix1, matrix2))

print("\nMatrix Transpose")
print(matrix1.T)

print("\nMatrix Shape")
print(matrix1.shape)

print("\nMatrix Sum")
print(np.sum(matrix1))

print("\nUnique Passenger Classes")
print(np.unique(data["Pclass"]))

print("\nTotal Passengers")
print(len(data))

print("\nTotal Survivors")
print(data["Survived"].sum())

print("\nSurvival Rate")
print((data["Survived"].sum()/len(data))*100)