from keras.models import Sequential
from keras.preprocessing import sequence
from keras.layers import Dense, Embedding
from keras.layers import LSTM
import matplotlib.pyplot as plt

import numpy as np

data_end = 6000

train_end = 8200

dataset = np.loadtxt("data/processed_data_pi.txt", delimiter=" ")


inputData = dataset[0:data_end, 0:6]
inputData = np.reshape(inputData, (inputData.shape[0], 1, inputData.shape[1]))
outputData = dataset[0:data_end, 6:9] # use more data

iTrainData = dataset[data_end:train_end, 0:6]
iTrainData = np.reshape(iTrainData, (iTrainData.shape[0], 1, iTrainData.shape[1]))

oTrainData = dataset[data_end:train_end, 6:9]

model = Sequential()
model.add(LSTM(6, return_sequences=True))
model.add(LSTM(3))
model.add(Dense(3, activation='softmax'))

model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['categorical_accuracy'])
history = model.fit(inputData, outputData, epochs=30, batch_size=100, validation_data=(iTrainData, oTrainData)) # change this to higher when using more data

model_json = model.to_json()
with open("keras/model.json", "w") as json_file:
	json_file.write(model_json)
model.save_weights("keras/model.h5")
