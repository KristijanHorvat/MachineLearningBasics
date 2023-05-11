import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn . model_selection import train_test_split
from sklearn . linear_model import LogisticRegression
from sklearn . metrics import accuracy_score, classification_report, precision_score, recall_score
from sklearn . metrics import confusion_matrix , ConfusionMatrixDisplay
import matplotlib.pyplot as plt

data = np.loadtxt("pima-indians-diabetes.csv", skiprows=9, delimiter=",")

data_df = pd.DataFrame(data, columns=['num_pregnant', 'plasma', 'blood_pressure', 'triceps', 'insulin', 'BMI', 'diabetes_function', 'age', 'diabetes'])
X=data_df.drop(columns=["diabetes"]).to_numpy()
Y=data_df["diabetes"].copy().to_numpy()

X_train , X_test , y_train , y_test = train_test_split(X , Y , test_size = 0.2 , random_state = 5 )
#A)
LogRegression_model = LogisticRegression()
LogRegression_model.fit(X_train, y_train)
#B)
y_test_p=LogRegression_model.predict(X_test)
#C)
disp = ConfusionMatrixDisplay ( confusion_matrix ( y_test , y_test_p ) )
disp . plot ()
plt . show ()
#D)
print(classification_report(y_test , y_test_p))
print(accuracy_score(y_test , y_test_p))
print(precision_score(y_test , y_test_p))
print(recall_score(y_test , y_test_p))