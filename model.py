import numpy as np
from processing import *
from sklearn.model_selection import KFold
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.optimizers import SGD

def define_model():
	model = Sequential()
	model.add(Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform', input_shape=(100, 100, 1)))
	model.add(MaxPooling2D((2, 2)))
	model.add(Flatten())
	model.add(Dense(100, activation='relu', kernel_initializer='he_uniform'))
	model.add(Dense(1000, activation='relu', kernel_initializer='he_uniform'))
	model.add(Dense(10000, activation='relu', kernel_initializer='he_uniform'))
	model.add(Dense(35000, activation='relu', kernel_initializer='he_uniform'))
	model.add(Dense(65259, activation='softmax'))
	opt = SGD(learning_rate=0.01, momentum=0.9)
	model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
	return model

def evaluate_model(dataX, dataY, n_folds=5):
#def evaluate_model(trainX, trainY, testX, testY):
	#model = define_model()
	#model.fit(trainX, trainY, epochs=10, batch_size=32, validation_data=(testX, testY), verbose=2)
	#_, acc = model.evaluate(testX, testY, verbose=1)
	#print('> %.3f' % (acc * 100.0))
	kfold = KFold(n_folds, shuffle=True, random_state=1)
	for train_ix, test_ix in kfold.split(dataX):
		model = define_model()
		trainX, trainY = dataX[train_ix], dataY[train_ix]
		testX, testY = dataX[test_ix], dataY[test_ix]
		model.fit(trainX, trainY, epochs=10, batch_size=32, validation_data=(testX, testY), verbose=1)
		_, acc = model.evaluate(testX, testY, verbose=1)
		print('> %.3f' % (acc * 100.0))

def run_test_harness():
	trainX, trainY, testX, testY = collect_data()
	trainX = np.array(trainX)
	trainY = np.array(trainY)
	testX = np.array(testX)
	testY = np.array(testY)
	trainX = trainX.reshape(-1, 100, 100, 1)
	testX = testX.reshape(-1, 100, 100, 1)
	trainY = to_categorical(trainY)
	testY = to_categorical(testY)

	print("training!!")
	evaluate_model(trainX, trainY)

run_test_harness()