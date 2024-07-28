# scikit_neutrosophic/neutrosophic_linear_regression.py

import numpy as np

class NeutrosophicLinearRegression:
    def __init__(self, learning_rate=0.01, epochs=1000):
        self.learning_rate = learning_rate
        self.epochs = epochs

    def fit(self, X, y, neutrosophic_params):
        self.X_train = X
        self.y_train = y
        self.neutrosophic_params = neutrosophic_params
        self.a = 0
        self.b = 0
        self.train()

    def train(self):
        N = len(self.y_train)
        for _ in range(self.epochs):
            y_pred = self.a * self.X_train + self.b
            error = y_pred - self.y_train
            self.a -= self.learning_rate * (1/N) * np.dot(error, self.X_train)
            self.b -= self.learning_rate * (1/N) * np.sum(error)

    def predict(self, X):
        return self.a * X + self.b
