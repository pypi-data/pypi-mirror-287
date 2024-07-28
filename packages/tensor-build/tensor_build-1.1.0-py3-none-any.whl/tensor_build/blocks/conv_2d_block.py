import tensorflow as tf

class Conv2DBlock:
    def __init__(self, filters, kernel_size, strides=(1, 1), padding='valid', activation=None):
        self.filters = filters
        self.kernel_size = kernel_size
        self.strides = strides
        self.padding = padding
        self.activation = activation
        
        # Initialize Conv2D layer
        self.conv_layer = tf.keras.layers.Conv2D(
            filters=self.filters,
            kernel_size=self.kernel_size,
            strides=self.strides,
            padding=self.padding,
            use_bias=True
        )
        
        if self.activation:
            self.activation_layer = tf.keras.layers.Activation(self.activation)
        else:
            self.activation_layer = None

    def apply(self, inputs):
        x = self.conv_layer(inputs)
        if self.activation_layer:
            x = self.activation_layer(x)
        return x

    def get_config(self):
        config = {
            'filters': self.filters,
            'kernel_size': self.kernel_size,
            'strides': self.strides,
            'padding': self.padding,
            'activation': self.activation
        }
        return config
