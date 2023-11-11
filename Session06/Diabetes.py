import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x,y = load_diabetes(return_X_y=True, as_frame=True)
print(x)
print(y)

x.drop(columns=["sex","s4"],inplace=True)

model = LinearRegression()

features = x.columns

for i in range(len(features)):
    plt.subplot(1,len(features),i+1)
    plt.scatter(np.arange(len(x[features[i]].values)),x[features[i]])
    plt.title(features[i])


plt.show()

model.fit(x,y)
print(f"Total score: {model.score(x,y)*100}")

for feature in features:
    model.fit(x[feature].values.reshape(-1,1),y)
    print(x[feature].name,model.score(x[feature].values.reshape(-1,1),y)*100)