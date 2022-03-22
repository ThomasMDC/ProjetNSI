from keras.models import load_model
import numpy as np
from glob import glob
import cv2
import time
model = load_model("SurementUnScam.h5")
images = glob("GraphesTest/*")
for image in images:
    print(image)
    image = cv2.imread(image, cv2.IMREAD_COLOR)
    image = cv2.resize(image, (256, 256))
    image = image.reshape((1, 256, 256, 3))
    image = image.astype("float32")
    image /= 255
    image = np.asarray(image)
    prediction = model.predict(image)
    reponse = np.argmax(prediction)
    if reponse == 0:
        print("monte")
    else:
        print("descend")
    time.sleep(1)
#de 17h59 à 18h59 (dimanche) SurementUnScam avait raison (pas l'autre)