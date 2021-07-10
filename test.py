import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns

data_test = pd.read_csv("loan_data_test.csv")
print(data_test)

data_train = pd.read_csv("loan_data_train.csv")
print(data_train)

print(data_test.shape)
print(data_test.info())
print(data_test.describe().transpose)
print(data_test.head(10))
print(data_test.tail(10))


print(data_train.shape)
print(data_train.info())
print(data_train.describe().transpose)
print(data_train.head(5))
print(data_train.tail(5))