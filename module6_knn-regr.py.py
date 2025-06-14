import numpy as np

class KNNRegressor:
    """k-Nearest Neighbors Regressor using NumPy for efficient data processing"""
    
    def __init__(self):
        """Initialize the regressor with empty data"""
        self.points = None
        self.n_points = 0
    
    def initialize_data(self, n):
        """Initialize numpy array to store N points"""
        self.n_points = n
        self.points = np.zeros((n, 2))  # N x 2 array for (x, y) points
    
    def insert_point(self, index, x, y):
        """Insert a point at given index"""
        if self.points is not None and 0 <= index < self.n_points:
            self.points[index] = [x, y]
    
    def predict(self, x_query, k):
        """Perform k-NN regression to predict y for given x"""
        if k > self.n_points:
            raise ValueError("k cannot be greater than the number of training points")
        
        # Calculate Euclidean distances from query point to all training points
        x_coords = self.points[:, 0]  # Extract x coordinates
        distances = np.abs(x_coords - x_query)  # For 1D, use absolute distance
        
        # Find indices of k nearest neighbors
        k_nearest_indices = np.argpartition(distances, k-1)[:k]
        
        # Get y values of k nearest neighbors
        k_nearest_y = self.points[k_nearest_indices, 1]
        
        # Return mean of k nearest y values
        return np.mean(k_nearest_y)

def main():
    """Main program function"""
    try:
        # Get number of points
        N = int(input("Enter N (number of points): "))
        if N <= 0:
            print("Error: N must be a positive integer")
            return
        
        # Get k value
        k = int(input("Enter k (number of nearest neighbors): "))
        if k <= 0:
            print("Error: k must be a positive integer")
            return
        
        # Initialize regressor
        regressor = KNNRegressor()
        regressor.initialize_data(N)
        
        # Read N points
        print(f"Enter {N} points (x, y):")
        for i in range(N):
            try:
                x = float(input(f"Point {i+1} - Enter x: "))
                y = float(input(f"Point {i+1} - Enter y: "))
                regressor.insert_point(i, x, y)
            except ValueError:
                print("Error: Please enter valid real numbers")
                return
        
        # Get query point X
        try:
            X = float(input("Enter X for prediction: "))
        except ValueError:
            print("Error: Please enter a valid real number for X")
            return
        
        # Perform k-NN regression
        try:
            Y = regressor.predict(X, k)
            print(f"Result (Y): {Y}")
        except ValueError as e:
            print(f"Error: {e}")
    
    except ValueError:
        print("Error: Please enter valid integers for N and k")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()