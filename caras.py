import face_recognition
import keras
import tensorflow
import cv2
from keras.models import load_model
from PIL import Image
import numpy as np
import sys

#Cargar imagen
image = face_recognition.load_image_file(sys.argv[1]) #First argument is file name

#Recortar imagen
face_locations = face_recognition.face_locations(image)
top, right, bottom, left = face_locations[0]
face_image = image[top:bottom, left:right]

#Mostrar imagen recortada
img = Image.fromarray(face_image, 'RGB')
img.show()

model = load_model("./face_and_emotion_detection/emotion_detector_models/model_v6_23.hdf5")

#Redimensionar y retocar la imagen
face_image = cv2.resize(face_image, (48,48))
face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)

#Mostrar imagen retocada
img = Image.fromarray(face_image)
img.show()

face_image = np.reshape(face_image, [1, face_image.shape[0], face_image.shape[1], 1])

#Predecir imagen
predicted_class = np.argmax(model.predict(face_image))

#Obtener etiqueta correspondiente
emotion_dict= {'Angry': 0, 'Sad': 5, 'Neutral': 4, 'Disgust': 1, 'Surprise': 6, 'Fear': 2, 'Happy': 3}
label_map = dict((v,k) for k,v in emotion_dict.items()) 
predicted_label = label_map[predicted_class]
print(predicted_label)
