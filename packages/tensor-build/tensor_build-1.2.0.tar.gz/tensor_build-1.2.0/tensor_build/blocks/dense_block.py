import tensorflow as tf
class DenseBlock:
    def __init__(self, units, activation=None):
        self.units = units
        self.activation = activation
        self.layer = tf.keras.layers.Dense(units, activation=activation)

    def apply(self, inputs):
        return self.layer(inputs)

    def get_config(self):
        return {
            'units': self.units,
            'activation': self.activation
        }
