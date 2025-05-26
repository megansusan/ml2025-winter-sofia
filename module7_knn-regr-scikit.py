import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

def main():
    try:
        # Get N (number of points)
        N = int(input("Enter N (positive integer): "))
        if N <= 0:
            print("Error: N must be a positive integer")
            return
        
        # Get k (number of neighbors)
        k = int(input("Enter k (positive integer): "))
        if k <= 0:
            print("Error: k must be a positive integer")
            return
        
        # Check if k <= N
        if k > N:
            print("Error: k must be less than or equal to N")
            return
        
        # Initialize numpy arrays for data storage
        X_train = np.zeros((N, 1))  # Features (x values)
        y_train = np.zeros(N)       # Labels (y values)
        
        # Read N points
        print(f"Enter {N} points (x, y):")
        for i in range(N):
            print(f"Point {i+1}:")
            x = float(input("  Enter x value: "))
            y = float(input("  Enter y value: "))
            
            # Store data using numpy
            X_train[i, 0] = x
            y_train[i] = y
        
        # Calculate variance of labels in training dataset
        variance = np.var(y_train, ddof=0)  # Population variance
        print(f"\nVariance of labels in training dataset: {variance:.6f}")
        
        # Create and train k-NN regressor using scikit-learn
        knn_regressor = KNeighborsRegressor(n_neighbors=k)
        knn_regressor.fit(X_train, y_train)
        
        # Get input X for prediction
        X_test = float(input("\nEnter X value for prediction: "))
        
        # Make prediction using scikit-learn
        X_test_array = np.array([[X_test]])  # Convert to proper shape for sklearn
        y_pred = knn_regressor.predict(X_test_array)
        
        # Output the result
        print(f"k-NN Regression result (Y): {y_pred[0]:.6f}")
        
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()