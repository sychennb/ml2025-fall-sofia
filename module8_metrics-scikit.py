import numpy as np
from sklearn.metrics import precision_score, recall_score

class ClassificationData:
    def __init__(self):
        self.X = np.array([], dtype=int) 
        self.Y = np.array([], dtype=int) 

    def insert_points(self, N):
        self.X = np.zeros(N, dtype=int)
        self.Y = np.zeros(N, dtype=int)
        
        for i in range(N):
            x_val = int(input(f"Enter ground truth label (0 or 1) for point {i+1}: "))
            y_val = int(input(f"Enter predicted label (0 or 1) for point {i+1}: "))
            self.X[i] = x_val
            self.Y[i] = y_val

    def compute_metrics(self):
        precision = precision_score(self.X, self.Y, zero_division=0)
        recall = recall_score(self.X, self.Y, zero_division=0)
        return precision, recall

def main():
    N = int(input("Enter a positive integer N (number of points): "))
    
    data = ClassificationData()
    data.insert_points(N)
    
    precision, recall = data.compute_metrics()
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")

if __name__ == "__main__":
    main()