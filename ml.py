import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,accuracy_score

df = pd.read_csv('fd.csv')
X = df[['source ip', 'destination ip', 'source port ', 'destination port','length']]
Y = df['class']
x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.3,random_state=101)
lg = LogisticRegression()
lg.fit(x_train,y_train)
pred = lg.predict(x_test)
print(confusion_matrix(y_test,pred))
print(accuracy_score(y_test,pred))



