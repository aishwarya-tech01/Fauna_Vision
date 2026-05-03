import tensorflow as tf
from tensorflow.keras import layers, models

# 1. Load and Prepare Images
train_ds = tf.keras.utils.image_dataset_from_directory(
  'data',
  validation_split=0.2, # Save 20% of images for a final "test"
  subset="training",
  seed=123,
  image_size=(180, 180),
  batch_size=32)

val_ds = tf.keras.utils.image_dataset_from_directory(
  'data',
  validation_split=0.2,
  subset="validation",
  seed=123,
  image_size=(180, 180),
  batch_size=32)

# 2. Build the Brain (Neural Network)
model = models.Sequential([
  layers.Rescaling(1./255, input_shape=(180, 180, 3)),
  
  # Pehli Layer
  layers.Conv2D(16, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  
  # --- YE NAYI LAYERS ADD KAREIN ---
  layers.Conv2D(32, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  layers.Conv2D(64, 3, padding='same', activation='relu'),
  layers.MaxPooling2D(),
  # --------------------------------
  
  layers.Flatten(),
  layers.Dense(128, activation='relu'),
  layers.Dense(6, activation='softmax') # 6 animals ke liye
])

# 3. Compile and Train
model.compile(optimizer='adam',
loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False), # False karein             
 metrics=['accuracy'])

model.fit(train_ds, validation_data=val_ds, epochs=30)


model.save('fauna_model.h5')
print("Model trained and saved!")


