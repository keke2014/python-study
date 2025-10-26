import time
import functools

def timing_decorator(func):
    """
    A decorator that measures the execution time of a function.
    
    Args:
        func: The function to be decorated
    
    Returns:
        The wrapped function with timing functionality
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.6f} seconds")
        return result
    return wrapper

# Alternative implementation with more detailed output
def advanced_timing_decorator(func):
    """
    An advanced decorator that measures execution time with more detailed output.
    
    Args:
        func: The function to be decorated
    
    Returns:
        The wrapped function with timing functionality
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # More precise timing
        try:
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            print(f"[TIMING] Function '{func.__name__}' executed in {execution_time:.6f} seconds")
            return result
        except Exception as e:
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            print(f"[TIMING] Function '{func.__name__}' failed after {execution_time:.6f} seconds with error: {e}")
            raise
    return wrapper

# Example functions to demonstrate the decorator
@timing_decorator
def slow_function():
    """A function that simulates some work by sleeping for 1 second."""
    time.sleep(1)
    return "Slow function completed"

@timing_decorator
def calculate_sum(n):
    """Calculate the sum of numbers from 1 to n."""
    return sum(range(1, n + 1))

@advanced_timing_decorator
def fibonacci(n):
    """Calculate the nth Fibonacci number recursively."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
if __name__ == "__main__":
    print("Testing timing decorator:")
    
    # Test slow function
    result1 = slow_function()
    print(f"Result: {result1}\n")
    
    # Test calculation function
    result2 = calculate_sum(1000000)
    print(f"Sum result: {result2}\n")
    
    # Test recursive function with advanced decorator
    result3 = fibonacci(10)
    print(f"Fibonacci result: {result3}\n")