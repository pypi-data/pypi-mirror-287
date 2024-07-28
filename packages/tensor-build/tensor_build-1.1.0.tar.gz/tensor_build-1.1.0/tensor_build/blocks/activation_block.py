import tensorflow as tf

class ActivationBlock:
    def __init__(self, activation):
        self.activation = activation
        self.layer = tf.keras.layers.Activation(activation)

    def apply(self, inputs):
        return self.layer(inputs)

    def get_config(self):
        return {
            'activation': self.activation
        }

