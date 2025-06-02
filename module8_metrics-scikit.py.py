import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    # Get number of points from user
    N = int(input("Enter the number of points (N): "))
    
    # Initialize numpy arrays to store the data
    ground_truth = np.zeros(N, dtype=int)  # X values (ground truth)
    predictions = np.zeros(N, dtype=int)   # Y values (predictions)
    
    # Read N points from user
    print(f"Enter {N} points (x, y) where x is ground truth and y is prediction:")
    for i in range(N):
        print(f"Point {i+1}:")
        x = int(input("  Enter x (ground truth, 0 or 1): "))
        y = int(input("  Enter y (prediction, 0 or 1): "))
        
        # Store in numpy arrays
        ground_truth[i] = x
        predictions[i] = y
    
    # Calculate Precision and Recall using Scikit-learn
    precision = precision_score(ground_truth, predictions, zero_division=0)
    recall = recall_score(ground_truth, predictions, zero_division=0)
    
    # Output results
    print(f"\nResults:")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")

if __name__ == "__main__":
    main()