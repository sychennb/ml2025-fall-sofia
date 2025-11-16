import numpy as np
from sklearn.neighbors import KNeighborsRegressor

class KNNRegression:
    def __init__(self):
        self.X_train = np.array([]) 
        self.Y_train = np.array([])
        self.model = None

    def insert_points(self, N):
        self.X_train = np.zeros((N, 1), dtype=float)
        self.Y_train = np.zeros(N, dtype=float)
        for i in range(N):
            x_val = float(input(f"Enter x for point {i + 1}: "))
            y_val = float(input(f"Enter y for point {i + 1}: "))
            self.X_train[i] = x_val
            self.Y_train[i] = y_val

    def predict(self, X, k):
        if k > len(self.X_train):
            return "Error: k cannot be larger than the number of training points."
        self.model = KNeighborsRegressor(n_neighbors=k)
        self.model.fit(self.X_train, self.Y_train)
        Y_pred = self.model.predict(np.array([[X]]))
        return Y_pred[0]
    
    def label_variance(self):
        return np.var(self.Y_train)

def main():
    N = int(input("Enter a positive integer N (number of points): "))
    k = int(input("Enter a positive integer k (number of neighbors): "))

    knn = KNNRegression()
    knn.insert_points(N)
    
    X = float(input("Enter the X value to predict Y: "))
    result = knn.predict(X, k)

    print(f"Predicted Y: {result}")

    print(f"Variance of labels: {knn.label_variance()}")

if __name__ == "__main__":
    main()
