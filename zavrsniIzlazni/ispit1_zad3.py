from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix
from sklearn.model_selection import train_test_split
from tensorflow import keras
from keras . models import load_model

data = np.loadtxt("pima-indians-diabetes.csv", skiprows=9, delimiter=",")

data_df = pd.DataFrame(data, columns=['num_pregnant', 'plasma', 'blood_pressure', 'triceps', 'insulin', 'BMI', 'diabetes_function', 'age', 'diabetes'])
X=data_df.drop(columns=["diabetes"]).to_numpy()
Y=data_df["diabetes"].copy().to_numpy()

X_train , X_test , y_train , y_test = train_test_split(X , Y , test_size = 0.2 , random_state = 5 )

#A)

model = keras . Sequential ()
model.add ( keras.layers . Input ( shape = (8 , ) ) )
model.add ( keras.layers . Dense (12 , activation = "relu" ) )
model.add ( keras.layers . Dense (8 , activation = "relu" ) )
model.add ( keras.layers . Dense (1 , activation = "sigmoid" ) )
model.summary ()

#B)
model.compile ( loss = "binary_crossentropy" , optimizer = "adam" ,metrics = [ "accuracy" ,] )
#C)
history = model . fit ( X_train ,y_train ,batch_size = 10 ,epochs = 150,validation_split = 0.1 )
#D)
model.save("Model/")
#E)
model = load_model("Model/")
#E)
score = model.evaluate(X_test, y_test, verbose=0)
for i in range(len(model.metrics_names)):
    print(f'{model.metrics_names[i]} = {score[i]}')
#F)
predictions = model.predict(X_test)
y_predictions = model.predict(X_test)
y_predictions = np.around(y_predictions).astype(np.int32)
cm = confusion_matrix(y_test, y_predictions)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.show()
