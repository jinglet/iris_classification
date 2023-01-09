from sklearn.datasets import load_iris
import pandas as pd
import numpy as np

iris_data = load_iris()
#print(iris_data.keys())
#print(iris_data['feature_names'], iris_data['target_names'])

iris_data = pd.DataFrame(data=iris_data['data'], columns=iris_data['feature_names'])

iris_data.to_csv('iris.csv')
print(iris_data)
