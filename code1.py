from sklearn.datasets import load_iris
import pandas as pd
import numpy as np

iris_data = load_iris()
print(iris_data.keys())

iris_data = pd.DataFrame(data=iris_data['data'])

iris_data.to_csv('iris.csv')
