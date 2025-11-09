import numpy as np

class KNNRegression:
    def __init__(self):
        self.X_train = np.array([])
        self.Y_train = np.array([])

    def insert_points(self, N):
        self.X_train = np.zeros(N, dtype=float)
        self.Y_train = np.zeros(N, dtype=float)
        for i in range(N):
            x_val = float(input(f"Enter x for point {i + 1}: "))
            y_val = float(input(f"Enter y for point {i + 1}: "))
            self.X_train[i] = x_val
            self.Y_train[i] = y_val

    def predict(self, X, k):
        if k > len(self.X_train):
            return "Error: k cannot be larger than the number of training points."
        distances = np.abs(self.X_train - X)
        nearest_indices = np.argsort(distances)[:k]
        return np.mean(self.Y_train[nearest_indices])

def main():
    N = int(input("Enter a positive integer N (number of points): "))
    k = int(input("Enter a positive integer k (number of neighbors): "))

    knn = KNNRegression()
    knn.insert_points(N)

    X = float(input("Enter the X value to predict Y: "))
    result = knn.predict(X, k)

    print(f"Predicted Y: {result}")

if __name__ == "__main__":
    main()
