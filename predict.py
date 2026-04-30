import tensorflow as tf
import numpy as np

# 1. Load the model you just trained
model = tf.keras.models.load_model('fauna_model.h5')

# 2. Pick an image to test 
# (Make sure 'test_animal.jpg' exists in your folder or use an image from 'data')
img_path = 'data/jaguar/jaguar (1).jpeg' 

img = tf.keras.utils.load_img(img_path, target_size=(180, 180))
img_array = tf.keras.utils.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)

# 3. Predict!
predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

# 4. Show the result
class_names = ['capybara', 'jaguar', 'macaw']
print(f"This image most likely belongs to {class_names[np.argmax(score)]} with a {100 * np.max(score):.2f} percent confidence.")