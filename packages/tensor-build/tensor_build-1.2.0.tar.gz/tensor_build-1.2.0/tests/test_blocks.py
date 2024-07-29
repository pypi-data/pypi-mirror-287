import unittest
from tensor_build.blocks.conv_2d_block import Conv2DBlock

class TestBlock(unittest.TestCase):
    def test_block_initialization(self):
        block = Conv2DBlock(filters=32, kernel_size=(3, 3), activation='relu')
        self.assertEqual(block.filters, 32)
        self.assertEqual(block.kernel_size, (3, 3))
        self.assertEqual(block.activation, 'relu')

if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     # Create a simple model for demonstration purposes
#     model = tf.keras.models.Sequential([
#         tf.keras.layers.Flatten(input_shape=(28, 28)),
#         tf.keras.layers.Dense(128, activation='relu'),
#         tf.keras.layers.Dense(10)
#     ])

#     # Instantiate the CompileBlock with the model
#     compile_block = CompileBlock(model)

#     # Compile the model
#     compile_block.compile_model()

#     # Print model summary
#     compile_block.model_summary()

#     # Example training data (using random data for demonstration)
#     x_train = tf.random.normal((60000, 28, 28))
#     y_train = tf.random.uniform((60000,), maxval=10, dtype=tf.int32)

#     # Fit the model
#     compile_block.fit_model(x_train, y_train, epochs=5)