import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

filename = 'finalized_model.sav'

fashionmnist = keras.datasets.fashion_mnist

(train_images,train_labels),(test_images,test_labels) = fashionmnist.load_data()
np.set_printoptions(precision=3)
print(train_images.shape)
print(len(train_labels))

train_images = train_images / 255.0 # scaling data from 0 to 1
test_images = test_images / 255.0

def create_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')

    ])

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

# model = create_model()
#
# model.summary()
# model.save('my_model.h5')

loaded_model = tf.keras.models.load_model('my_model.h5')

loaded_model.fit(train_images,train_labels,epochs=10)



test_loss, test_acc = loaded_model.evaluate(test_images,test_labels,verbose=2)

print('Restored model, accuracy: {:5.2f}%'.format(100*test_acc))


# predictions = loaded_model.predict(test_images)
# print(predictions[2])
# classnum  = np.argmax(predictions[2])
# print(classnum)
#
# plt.figure(figsize=(10,10))
# plt.xticks([])
# plt.yticks([])
# plt.grid(False)
# plt.imshow(test_images[2])
# plt.show()


























