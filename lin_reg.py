
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
lr=LinearRegression()

nyc=pd.read_csv('ave_hi_nyc_jan_1895-2018.csv')

# print(nyc.head(10))


# print(nyc.Date.values)

# print(nyc.Date.values.reshape(-1,1))

# print(nyc.Temperature.values)



from sklearn.model_selection import train_test_split

data_train, data_test, target_train,target_test   =train_test_split(
nyc.Date.values.reshape(-1,1), nyc.Temperature.values, random_state=11
)

lr.fit(X=data_train, y= target_train)

coef=lr.coef_
intercept=lr.intercept_

predicted=lr.predict(X=data_test)

expected= target_test

print(predicted[:20])
print(expected[:20])


predict=lambda year: year*coef+intercept


print(predict(2025))


# print(data_train)


import seaborn as sns

axes=sns.scatterplot(
    data=nyc,
    x="Date",
    y="Temperature",
    palette="winter",
    legend=False

)

axes.set_ylim(10,70)
import numpy as np

x=np.array




