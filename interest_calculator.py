"""
Simple Interest Calculator Module

This module provides functions to calculate simple interest
and total amount based on principal, rate, and time.
"""

def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest earned on an investment or loan.
    
    Formula: Simple Interest = (Principal × Rate × Time) / 100
    
    Args:
        principal (float): The initial amount of money
        rate (float): Annual interest rate (as a percentage)
        time (float): Time period in years
    
    Returns:
        float: The simple interest earned/paid
    
    Raises:
        ValueError: If any input parameter is negative
    
    Example:
        >>> calculate_simple_interest(1000, 5, 2)
        100.0
    """
    # Validate input parameters to ensure they are non-negative
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("All parameters must be non-negative")
    
    # Calculate simple interest using standard formula
    interest = (principal * rate * time) / 100
    return interest


def calculate_total_amount(principal, rate, time):
    """
    Calculate total amount (principal + interest) after specified time.
    
    Args:
        principal (float): The initial amount of money
        rate (float): Annual interest rate (as a percentage)
        time (float): Time period in years
    
    Returns:
        float: Total amount after interest is applied
    
    Example:
        >>> calculate_total_amount(1000, 5, 2)
        1100.0
    """
    # Calculate interest using the previously defined function
    interest = calculate_simple_interest(principal, rate, time)
    
    # Total amount is principal plus earned interest
    total = principal + interest
    return total


def main():
    """
    Main function to demonstrate the simple interest calculator.
    This provides a command-line interface for user interaction.
    """
    print("=== Simple Interest Calculator ===\n")
    
    try:
        # Get user input with clear prompts
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter annual interest rate (%): "))
        time = float(input("Enter time period (years): "))
        
        # Validate that inputs are positive
        if principal <= 0 or rate <= 0 or time <= 0:
            print("Error: All values must be positive numbers.")
            return
        
        # Calculate and display results
        interest = calculate_simple_interest(principal, rate, time)
        total = calculate_total_amount(principal, rate, time)
        
        print("\n--- Results ---")
        print(f"Principal: ${principal:,.2f}")
        print(f"Interest Rate: {rate}%")
        print(f"Time: {time} years")
        print(f"Simple Interest: ${interest:,.2f}")
        print(f"Total Amount: ${total:,.2f}")
        
    except ValueError as e:
        # Handle invalid numeric input
        print(f"Error: Please enter valid numbers. {e}")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")


# Standard Python idiom to ensure main() runs only when script is executed directly
if __name__ == "__main__":
    main()