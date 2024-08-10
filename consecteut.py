def set_timeout(timeout):
    if timeout > 0:
        print(f"Timeout set to {timeout} seconds")
    else:
        raise ValueError("Timeout must be a positive number greater than zero.")

# Example usage
try:
    set_timeout(5)         # This is valid
    set_timeout(2.5)       # This is valid
    set_timeout(-1)        # This will raise an exception
    set_timeout(0)         # This will also raise an exception
except ValueError as e:
    print(e)
