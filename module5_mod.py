class NumberCollection:
    """A class to handle the collection of numbers and search operations."""
    
    def __init__(self):
        """Initialize an empty collection of numbers."""
        self.numbers = []
    
    def add_number(self, number):
        """Add a number to the collection.
        
        Args:
            number: The number to add to the collection.
        """
        self.numbers.append(number)
    
    def search_number(self, x):
        """Search for a number in the collection and return its index.
        
        Args:
            x: The number to search for.
            
        Returns:
            The 1-based index of the number if found, or -1 if not found.
        """
        for i, num in enumerate(self.numbers):
            if num == x:
                # Return 1-based index as per requirements
                return i + 1
        return -1
