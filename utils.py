import setting

def height_prct(percentage):
    """
    Calculate the height as a percentage of the total height from settings.

    Args:
        percentage (float): The percentage of the total height.

    Returns:
        float: The calculated height.
    """
    return (setting.height / 100) * percentage

# Example usage and print the result of height_prct(25)
print(height_prct(25))

def width_prct(percentage):
    """
    Calculate the width as a percentage of the total width from settings.

    Args:
        percentage (float): The percentage of the total width.

    Returns:
        float: The calculated width.
    """
    return (setting.width / 100) * percentage

# Example usage and print the result of width_prct(25)
print(width_prct(25))
