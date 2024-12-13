def reverse_list(my_list):
    """Reverses a list without using sort.

    Args:
      my_list: The list to reverse (required).

    Returns:
      A new list with the elements in reverse order.
    """
    return my_list[::-1]


# Example usage
original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list.copy())  # Avoid modifying original list
print(f"Original: {original_list}, Reversed: {reversed_list}")
