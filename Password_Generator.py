# Import random
import random
# Import string
import string

# Function to generate password
   # Parameters: length, include_letters, include_numbers, include_symbols
def generate_password(length, include_letters=True, include_numbers=True, include_symbols=True):
   # Create a string of characters for the password
    characters = ''
   # If include_letters is True, add the letters to the characters string
    if include_letters:
        characters += string.ascii_letters
   # If include_numbers is True, add the numbers to the characters string
    if include_numbers:
        characters += string.digits
   # If include_symbols is True, add the symbols to the characters string
    if include_symbols:
        characters += string.punctuation
    # If no characters are included, raise a ValueError
    if not characters:
        raise ValueError("At least one character type (letters, numbers, symbols) must be included.")
    # Generate a password with the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    # Return the password
    return password
# Main function to run the password generator
def main():
    # Print welcome message
    print("Welcome to the PyPassword Generator!\n")

    # Loop to generate passwords
    while True:
        # Try to get user input for password length and character types
        try:
            length = int(input("How many characters would you like in your password? (min. 6): "))
            # If the length is less than 6, raise a ValueError
            if length < 6:
                print("Password must be at least 6 characters long. Please try again.\n")
                # Continue to the next iteration of the loop
                continue
            # Get user input for character types
            include_letters = input("Include letters? (y/n): ").lower() == 'y'
            include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
            include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
            # Generate the password
            password = generate_password(length, include_letters, include_numbers, include_symbols)

            # Print the generated password
            print(f"\nYour generated password is: {password}\n")
            
            # Ask the user if they would like to generate another password
            another_password = input("Would you like to generate another password? (y/n): ").lower()
            # If the user wants to generate another password, continue to the next iteration of the loop
            if another_password != 'y':
                print("Goodbye! Thank you for using the PyPassword Generator!")
                break
        # Handle errors
            # If the user enters a non-integer value for the password length, raise a ValueError
        except ValueError as e:
            print(f"Error: {e}\n")
# Run the main function
if __name__ == "__main__":
    main()
