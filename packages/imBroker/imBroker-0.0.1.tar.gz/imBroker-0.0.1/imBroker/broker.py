import cv2, os
import numpy as np
import tensorflow as tf
from keras.utils import img_to_array

class tflBroker:
  def __init__(self, model_path, output_labels) -> None:
      self.output_labels = list(output_labels.values())
      self.model, self.input_details, self.output_details = self.initalise_model(model_path=model_path)
      self.input_shape = self.input_details[0]['shape'][1:4]  # This will be [height, width, channels]

  def initalise_model(self, model_path):
      interpreter = tf.lite.Interpreter(model_path=model_path)
      interpreter.allocate_tensors()

      input_details = interpreter.get_input_details()
      output_details = interpreter.get_output_details()

      return interpreter, input_details, output_details

  def convert_image_to_array(self, image_path):
      try:
          image = cv2.imread(image_path)
          if image is not None:
              # Resize image
              image = cv2.resize(image, (self.input_shape[1], self.input_shape[0]))  # width, height
              
              # Convert to grayscale if the model expects 1 channel
              if self.input_shape[2] == 1:
                  image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                  image = np.expand_dims(image, axis=-1)
              else:
                  image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # OpenCV uses BGR, convert to RGB
              
              image_array = img_to_array(image)
              image_array = np.array(image_array, dtype=np.float32) / 255
              image_array = image_array.reshape(-1, self.input_shape[0], self.input_shape[1], self.input_shape[2])
              return image_array
          else:
              return np.array([])
      except Exception as e:
          print(f"Error : {e}")
          return None
  
  def process_image(self, inputImageDir):
    inputImage = self.convert_image_to_array(inputImageDir)
    
    self.model.set_tensor(self.input_details[0]['index'], inputImage)
    self.model.invoke()

    prediction = self.model.get_tensor(self.output_details[0]['index'])

    return self.output_labels[np.argmax(prediction)]
  
  def predict_single_image(self, inputPath):
    prediction = self.process_image(inputPath)
    
    result = {
      "input_directory": inputPath,
      "prediction": prediction
    }
    
    return result
  
  def predict_image_directory(self, inputDirectory):
    images = os.listdir(inputDirectory)
    predictions = {}
    
    for idx, image in enumerate(images):
      image_path = os.path.join(inputDirectory, image)
      prediction = self.process_image(image_path)
      predictions[idx] = prediction
    
    result = {
      "input_directory": inputDirectory,
      "predictions": predictions
    }
    
    return result