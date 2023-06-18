# # import obd
# import cv2
# import time
# #import pyttxs3
# import requests
# import numpy as np
# from PIL import Image
# from keras.models import load_model
# # ==========================================================================>
# connection = obd.OBD("COM5")

# model = load_model('model.h5',compile=False)

# class_labels = ['Drinking','hair and makeup','Turn on radio','look behind','Driving safe','Talk with left','Talk with right','talking passenger','Texting left','Texting right']

# class_attentions = "Please Focus on Your Driving"

# url = "https://mcv-pro.herokuapp.com/api/my-car/1"
# # ==========================================================================>
# def image_preprocess(im):
#     # Convert the frame to a PIL Image
#     image = Image.fromarray(frame)

#     # Resize the image to the required input size of the model
#     image = image.resize((280, 200))

#     # Convert the image to a numpy array
#     image_array = np.array(image)

#     # Expand the dimensions of the array to match the expected input shape of the model
#     image_array = np.expand_dims(image_array, axis=0)

#     # Normalize the pixel values of the image
#     image_array = image_array / 255.0

#     # Make predictions using the loaded model
#     predictions = model.predict(image_array)

#     # Get the predicted class and its probability
#     predicted_class_index = np.argmax(predictions[0])
#     predicted_class = class_labels[predicted_class_index]
#     accuracy = predictions[0][predicted_class_index]
#     return predicted_class,accuracy
# # ==========================================================================>
# """
# def Say(text):
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 160)
#     engine.setProperty('volume', 0.8)
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice', voices[0].id)
#     engine.say(str(text))
#     engine.runAndWait()
# """
# # ==========================================================================>
# font = cv2.FONT_HERSHEY_SIMPLEX
# font_scale = 0.75
# text_color = (0, 255, 0)
# cap = cv2.VideoCapture(0)
# # ==========================================================================>
# while True:
    
#     context={}
#     # ==========================================================================>
#     ret, frame = cap.read()
#     predicted_class,accuracy=image_preprocess(frame)
#     # ==========================================================================>
#     """if predicted_class != "Driving safe":
#         Say(class_attentions)
#     # ==========================================================================>
#     """
    
#     border_color = (0, 255, 0)
#     border_size = 2
#     # ==========================================================================>
#     frame = cv2.rectangle(frame, (0, 0), (frame.shape[1], frame.shape[0]), border_color, border_size)
#     # ==========================================================================>
#     text = f"{predicted_class} ({accuracy:.2f})"
#     text_size, _ = cv2.getTextSize(text, font, font_scale, border_size)
#     text_x = int((frame.shape[1] - text_size[0]) / 2)
#     text_y = int(frame.shape[0] - text_size[1] - 10)
#     # ==========================================================================>
#     frame = cv2.putText(frame, text, (text_x, text_y), font, font_scale, text_color, border_size)
#     # ==========================================================================>
#     context["rpm"]      = round(float(str(connection.query(obd.commands.RPM).value).split(" ")[0])/1000)
#     context["speed"]    = round(float(str(connection.query(obd.commands.SPEED).value).split(" ")[0]))
#     context["run_time"] = round(float(str(connection.query(obd.commands.RUN_TIME).value).split(" ")[0]))
#     context["distance"] = round(float(str(connection.query(obd.commands.DISTANCE_SINCE_DTC_CLEAR).value).split(" ")[0]))
#     context["temp"]     = round(float(str(connection.query(obd.commands.COOLANT_TEMP).value).split(" ")[0]))
#     context["engine"]   = round(float(str(connection.query(obd.commands.ENGINE_LOAD).value).split(" ")[0]))
#     # ==========================================================================>
#     payload={ 
#                 'car_speed'         : 33,#context['speed'],
#                 'car_rpm'           : 33,#context['rpm'],
#                 'car_run_time'      : 33,#context['run_time'],
#                 'car_tempreture'    : 33,#context['temp'],
#                 'car_engine_load'   : 33,#context['engine'],
#                 'car_distance'      : 33,#context['distance'],
#                 'driver_action'     : predicted_class,
#             }
#     files=[]
#     # ==========================================================================>
#     headers = {'Authorization': 'Token 559cfd49ba25f5098e1006ef08ed07ad5e3c95e1'}
#     response = requests.request("PUT", url, headers=headers, data=payload, files=files)
#     # ==========================================================================>
#     cv2.imshow('Prediction', frame)
#     # ==========================================================================>
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#     # ==========================================================================>
#     time.sleep(2)

# cap.release()
# cv2.destroyAllWindows()



import requests

url = "https://mcv-pro.herokuapp.com/api/my-car/1/"

payload = {'car_speed': '100',
'car_rpm': '7.8',
'car_run_time': '14:22:45',
'car_tempreture': '30',
'car_engine_load': '50',
'car_distance': '300',
'driver_action': 'Texting right'}
files=[

]
headers = {
  'Authorization': 'Token 559cfd49ba25f5098e1006ef08ed07ad5e3c95e1'
}

response = requests.request("PUT", url, headers=headers, data=payload, files=files)

print(response.text)

