import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
import cv2
from tqdm import tqdm
from glob import glob
from sklearn.model_selection import train_test_split

X = []
X_train = []
X_test = []

Y = []
Y_train = []
Y_test = []

for image in tqdm(glob("Graphes/0*.jpg")):
    Y.append(0)
    im = cv2.imread(image, cv2.IMREAD_COLOR)
    im = im.astype("float32")
    im /= 255
    X.append(im)

for image in tqdm(glob("Graphes/1*.jpg")):
    Y.append(1)
    im = cv2.imread(image, cv2.IMREAD_COLOR)
    im = cv2.resize(im, (256,256))
    im = im.astype("float32")
    im /= 255
    X.append(im)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=42)
X_test = np.asarray(X_test)
Y_test = keras.utils.to_categorical(Y_test, 2)
X_train = np.asarray(X_train)
Y_train = keras.utils.to_categorical(Y_train, 2)

print(X_train.shape)
print(Y_train.shape)
print(X_test.shape)
print(Y_test.shape)
print(X_train)
print(Y_train)

model = keras.Sequential()
model.add(layers.Conv2D(25,input_shape=(640, 480, 3), activation='relu', kernel_size=(3, 3)))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))
model.add(layers.Conv2D(25, activation='relu', kernel_size=(3,3)))

model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dropout(0.2))
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dropout(0.2))
model.add(layers.Dense(2, activation='softmax'))

model.summary()

input()
model.compile(loss="categorical_crossentropy", optimizer="Adam", metrics=["accuracy"])
model.fit(X_train, Y_train, batch_size=64, epochs=20, validation_data=(X_test, Y_test))
model.save("g.h5")