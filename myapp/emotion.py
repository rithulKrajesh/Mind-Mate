# import numpy as np
# import argparse
# import cv2
# import os
# import tensorflow as tf
#
#
#
#
# model = tf.keras.models.load_model(r'D:\project\loneliness_detection\myapp\emotion_detection_model.h5')
# emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}
#
#
# # cap = cv2.VideoCapture(0)
# # while True:
#
# import keras.backend as K
# def predict_emo(fpath):
#     # Find haar cascade to draw bounding box around face
#     # ret, frame = cap.read()
#     # if not ret:
#     #     break
#     frame=cv2.imread(fpath)
#     facecasc = cv2.CascadeClassifier(r'D:\project\loneliness_detection\myapp\haarcascade_frontalface_default.xml')
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = facecasc.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
#     print("Faces ",len(faces))
#     if len(faces) > 0:
#         for (x, y, w, h) in faces:
#             cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (255, 0, 0), 2)
#             roi_gray = gray[y:y + h, x:x + w]
#             cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
#
#             prediction = model.predict(cropped_img)
#             K.clear_session()
#             maxindex = int(np.argmax(prediction))
#             # cv2.putText(frame, emotion_dict[maxindex], (x+20, y-60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
#             return emotion_dict[maxindex]
#     else:
#         return "Neutral"
#     # cv2.imshow('Video', cv2.resize(frame,(1600,960),interpolation = cv2.INTER_CUBIC))
#     # if cv2.waitKey(1) & 0xFF == ord('q'):
#     #     break
#
#
# # cap.release()
# # cv2.destroyAllWindows()



from deepface import DeepFace
def predict_emo(fpath):

    # Using DeepFace to analyze emotions
    result = DeepFace.analyze(fpath, actions=['emotion'])

    # Display the result
    print(result['emotion'])
    print(result['dominant_emotion'])
    return result['dominant_emotion']