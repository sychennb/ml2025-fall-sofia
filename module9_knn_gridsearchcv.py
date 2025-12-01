import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

class KNNClassificationData:
    def __init__(self):
        self.X_train = np.array([])
        self.Y_train = np.array([])
        self.X_test = np.array([])
        self.Y_test = np.array([])

    def insert_training_points(self, N):
        self.X_train = np.zeros((N, 1), dtype=float)
        self.Y_train = np.zeros(N, dtype=int)

        for i in range(N):
            x_val = float(input(f"Enter x for TRAIN point {i+1}: "))
            y_val = int(input(f"Enter y (class label) for TRAIN point {i+1}: "))
            self.X_train[i] = x_val
            self.Y_train[i] = y_val

    def insert_test_points(self, M):
        self.X_test = np.zeros((M, 1), dtype=float)
        self.Y_test = np.zeros(M, dtype=int)

        for i in range(M):
            x_val = float(input(f"Enter x for TEST point {i+1}: "))
            y_val = int(input(f"Enter y (class label) for TEST point {i+1}: "))
            self.X_test[i] = x_val
            self.Y_test[i] = y_val


def main():
    N = int(input("Enter N (number of TRAIN points): "))
    data = KNNClassificationData()
    data.insert_training_points(N)

    M = int(input("Enter M (number of TEST points): "))
    data.insert_test_points(M)


    model = KNeighborsClassifier()
    param_grid = {'n_neighbors': list(range(1, 11))}

    grid = GridSearchCV(
        estimator=model,
        param_grid=param_grid,
        scoring='accuracy',
        cv=5
    )
    grid.fit(data.X_train, data.Y_train)

    best_k = grid.best_params_['n_neighbors']
    print(f"\nBest k found via GridSearchCV: {best_k}")

    best_model = grid.best_estimator_
    y_pred = best_model.predict(data.X_test)
    test_accuracy = accuracy_score(data.Y_test, y_pred)
    print(f"Test Accuracy: {test_accuracy:.4f}")


if __name__ == "__main__":
    main()
