def calculate_discounted_price(price, discount):
    """
    Calculates the discounted price of a product given its original price and discount percentage.

    Args:
        price (float): The original price of the product.
        discount (float): The discount percentage as a decimal.

    Returns:
        float: The discounted price of the product.
    """
    # Calculate the discounted price
    discounted_price = price * (1 - discount)
    # Round the discounted price to two decimal places
    discounted_price = round(discounted_price, 2)
    # Return the discounted price
    return discounted_price
