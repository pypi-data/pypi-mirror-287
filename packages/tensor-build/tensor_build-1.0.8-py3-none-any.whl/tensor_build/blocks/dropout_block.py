import tensorflow as tf

class DropoutBlock:
    def __init__(self, rate):
        """
        Initializes the DropoutBlock with a Dropout layer.

        Args:
            The dropout rate, which is the fraction of input units to drop.
        """
        self.rate = rate
        self.layer = tf.keras.layers.Dropout(rate)

    def apply(self, inputs, training=False):
        return self.layer(inputs, training=training)

    def get_config(self):
        return {
            'rate': self.rate
        }
