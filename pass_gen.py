import string
import random

def pass_gen():
    while True:
        try:
            # Prompt for password length or exit
            user_input = input("Enter the desired length of the password or type 'exit' to quit: \n")
            if user_input.lower() == "exit":  # Corrected the method call
                break

            length = int(user_input)  # Convert input to integer
            if length < 1:
                print("Invalid input. The length must be at least 1.")
                continue

            # Ask user for character type preferences
            include_uppercase = input("Include uppercase letters in your password? (yes/no): \n").lower() == "yes"
            include_numbers = input("Include numbers in your password? (yes/no): \n").lower() == "yes"
            include_special = input("Include special characters in your password? (yes/no): ").lower() == "yes"

            # Initialize the character pool
            character_pool = string.ascii_lowercase  # Always include lowercase letters
            if include_uppercase:
                character_pool += string.ascii_uppercase
            if include_numbers:
                character_pool += string.digits
            if include_special:
                character_pool += string.punctuation

            # Validate character pool
            if not character_pool:
                print("No character types selected. Cannot generate a password. Please try again.")
                continue

            # Generate and display the password
            password = ''.join(random.choices(character_pool, k=length))
            print("\nGenerated Password:", password)
            break

        except ValueError:
            print("Invalid input. Please enter a valid number for the password length.")
            continue

    print("Thank you for using the password generator!")

# Run the function
pass_gen()
