import  tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_label),(test_images,test_label) = fashion_mnist.load_data()

train_images = train_images/255.0
test_images = test_images/255.0

model = keras.Sequential([
    keras.layers.Flatten(input_shape = (28,28)),
    keras.layers.Dense(128,activation='relu'),
    keras.layers.Dense(10)]
)

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(train_images,train_label,epochs=10)

test_loss, test_acc = model.evaluate(test_images,test_label,verbose=2)
print('accuracy',test_acc)

probability_model = tf.keras.Sequential([
    model,tf.keras.layers.Softmax()
])

prediction = probability_model.predict(test_images)

print(np.argmax(prediction[0]))
print(test_label[0])


def plot_image(i, prediction_array, true_label, img):
    prediction_array, true_label, img = prediction_array, true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img, cmap=plt.cm.binary)

    prediction_label = np.argmax(prediction_array)
    if prediction_label == true_label:
        color = 'blue'
    else:
        color = 'red'

    plt.xlabel("{} {:2.0f}% ({})".format(class_names[prediction_label],
                                         100*np.max(prediction_array),
                                         class_names[true_label]),
               color=color)


def plot_value_array(i, prediction_array,true_label):
    prediction_array, true_label = prediction_array, true_label[i]
    plt.grid(False)
    plt.xticks([10])
    plt.yticks([])

    thisplot = plt.bar(range(10),prediction_array, color = "#777777")
    plt.ylim([0,1])
    predicted_label = np.argmax(prediction_array)
    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')


i=0
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, prediction[i],test_label, test_images)
plt.subplot(1,2,2)
plot_value_array(i,prediction[i],test_label)
plt.show()











# plt.figure(figsize=(10,10))
# for i in range(25):
#     plt.subplot(5,5,i+1)
#     plt.xticks([])
#     plt.yticks([])
#     plt.grid(False)
#     plt.imshow(train_images[i],cmap=plt.cm.binary)
#     plt.xlabel(class_names[train_label[i]])
# plt.show()


