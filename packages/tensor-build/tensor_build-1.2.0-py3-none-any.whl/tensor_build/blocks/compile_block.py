import tensorflow as tf

class CompileBlock:
    def __init__(self, model):
        self.model = model

    def compile_model(self, optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy']):
        self.model.compile(optimizer=optimizer, loss=loss, metrics=metrics)
        return self.model

    def fit_model(self, x_train, y_train, epochs=10, batch_size=32, validation_data=None):
        history = self.model.fit(
            x_train, y_train,
            epochs=epochs,
            batch_size=batch_size,
            validation_data=validation_data
        )
        return history

    def model_summary(self):
        self.model.summary()