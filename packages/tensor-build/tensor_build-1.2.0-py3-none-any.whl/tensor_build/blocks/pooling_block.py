import tensorflow as tf

class PoolingBlock:
    def __init__(self, pool_size, strides=None, padding='valid', pool_type='max'):
        
        #Initializes the PoolingBlock.
        self.pool_size = pool_size
        self.strides = strides
        self.padding = padding
        self.pool_type = pool_type
        
        if self.pool_type == 'max':
            self.pooling_layer = tf.keras.layers.MaxPooling2D(
                pool_size=self.pool_size,
                strides=self.strides,
                padding=self.padding
            )
        elif self.pool_type == 'average':
            self.pooling_layer = tf.keras.layers.AveragePooling2D(
                pool_size=self.pool_size,
                strides=self.strides,
                padding=self.padding
            )
        else:
            raise ValueError("Invalid pool_type. Choose either 'max' or 'average'.")

    def apply(self, inputs):
        return self.pooling_layer(inputs)

    def get_config(self):
        return {
            'pool_size': self.pool_size,
            'strides': self.strides,
            'padding': self.padding,
            'pool_type': self.pool_type
        }
