import os
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

# Model load karein
model = load_model('fauna_model.h5')

# Purani line: img_size = (224, 224)
img_size = (180, 180) # Is nayi line se replace karein
# predict.py mein ise aise rakhein
class_names = ['anaconda', 'capybara', 'golden frogs', 'jaguar', 'macaw', 'tucan']
data_dir = 'data' 

print(f"{'Animal Folder':<15} | {'Predicted':<15} | {'Confidence'}")
print("-" * 50)

for folder in os.listdir(data_dir):
    folder_path = os.path.join(data_dir, folder)
    if os.path.isdir(folder_path):
        # Folder ke andar ki images check karein
        images = [f for f in os.listdir(folder_path) if f.endswith(('.jpeg', '.jpg', '.png'))]
        if images:
            img_path = os.path.join(folder_path, images[0])
            img = image.load_img(img_path, target_size=img_size)
            img_array = image.img_to_array(img) / 255.0
            img_array = np.expand_dims(img_array, axis=0)
            
            preds = model.predict(img_array, verbose=0)
            print(f"{folder:<15} | {class_names[np.argmax(preds)]:<15} | {np.max(preds)*100:.2f}%")