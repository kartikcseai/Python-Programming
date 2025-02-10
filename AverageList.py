# Write a python function named ComputeAverage to find average of a list of numbers. It should handle the exception if the list is empty and return 0 in that case. 

def ComputeAverage(numbers):
    try:
        if not numbers:  # Check if the list is empty
            return 0
        return sum(numbers) / len(numbers)
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

# Example usage
nums = [10, 20, 30, 40, 50]
print("Average:", ComputeAverage(nums))  # Output: 30.0

empty_list = []
print("Average:", ComputeAverage(empty_list))  # Output: 0
