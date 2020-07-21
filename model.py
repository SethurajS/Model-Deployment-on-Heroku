
""" IMPORTING THE REQUIREMENTS """

import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression


""" READING DATA SET CSV FILE  """

data = pd.read_csv("salary.csv")


""" FEATURE ENGINEERING """

print("\nBefore feature engineering : Nums of null values \n")
print(data.isnull().sum(), "\n\n")

data["Experience"] = data["Experience"].fillna(0)
data["Test_score"] = data["Test_score"].fillna(data["Test_score"].mean())

print("After feature engineering : Nums of null values  \n")
print(data.isnull().sum(), "\n")


""" CONVERT TEXT TO INT """

print(data.head(), "\n")


def convert_to_int(word):
    word_dict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8,
                'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'zero':0, 0: 0}
    return word_dict[word]

data['Experience'] = data['Experience'].apply(lambda x : convert_to_int(x))

print(data.head())


""" CREATING DEPENDENT AND INDEPENDENT DATA SET """

X = data.iloc[:, :3]
y = data.iloc[:, -1]

""" MODEL CREATION """

regressor = LinearRegression()
regressor.fit(X, y)


""" SAVING MODEL """

pickle.dump(regressor, open('model.pkl', 'wb'))


""" LOAD MODEL """

model = pickle.load(open('model.pkl', 'rb'))


""" PREDICTING """

print(np.round(model.predict([[2, 9, 6]]), 2))