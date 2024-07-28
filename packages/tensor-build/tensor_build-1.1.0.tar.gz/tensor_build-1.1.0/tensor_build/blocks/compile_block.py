# tensor_build/blocks/compile_block.py
import tensorflow as tf

class Compile:
    @staticmethod
    def compile_model(model):
        model.compile(
            optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']
        )
        return model

    @staticmethod
    def model_summary(model):
        model.summary()
