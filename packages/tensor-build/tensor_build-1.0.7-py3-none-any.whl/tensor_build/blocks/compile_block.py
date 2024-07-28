import tensorflow as tf
from tensorflow.python.keras.layers import layers, model


class Compile:
    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

    # Summary of the model
    model.summary()



# class Compile:
#     def __init__(self):
#         self.model = models.Sequential()
#         self.model.compile(optimizer='adam',
#                            loss='sparse_categorical_crossentropy',
#                            metrics=['accuracy'])

#         # Summary of the model
#         self.model.summary()