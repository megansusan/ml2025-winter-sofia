import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def main():
    # Read training set size
    print("Enter the number of training samples (N):")
    N = int(input())
    
    # Initialize training data arrays using NumPy
    train_X = np.zeros(N, dtype=float)
    train_y = np.zeros(N, dtype=int)
    
    # Read training data pairs
    print(f"Enter {N} training pairs (x, y):")
    for i in range(N):
        print(f"Training pair {i+1}:")
        print("Enter x value:")
        train_X[i] = float(input())
        print("Enter y value:")
        train_y[i] = int(input())
    
    # Read test set size
    print("Enter the number of test samples (M):")
    M = int(input())
    
    # Initialize test data arrays using NumPy
    test_X = np.zeros(M, dtype=float)
    test_y = np.zeros(M, dtype=int)
    
    # Read test data pairs
    print(f"Enter {M} test pairs (x, y):")
    for i in range(M):
        print(f"Test pair {i+1}:")
        print("Enter x value:")
        test_X[i] = float(input())
        print("Enter y value:")
        test_y[i] = int(input())
    
    # Reshape data for scikit-learn (expects 2D arrays)
    train_X = train_X.reshape(-1, 1)
    test_X = test_X.reshape(-1, 1)
    
    # Find the best k value by testing k from 1 to 10
    best_k = 1
    best_accuracy = 0.0
    
    print("\nTesting k values from 1 to 10:")
    for k in range(1, 11):
        # Create and train k-NN classifier
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(train_X, train_y)
        
        # Make predictions on test set
        predictions = knn.predict(test_X)
        
        # Calculate accuracy
        accuracy = accuracy_score(test_y, predictions)
        
        print(f"k = {k}: accuracy = {accuracy:.4f}")
        
        # Update best k if current accuracy is better
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_k = k
    
    # Output the results
    print(f"\nBest k: {best_k}")
    print(f"Corresponding test accuracy: {best_accuracy:.4f}")

if __name__ == "__main__":
    main()