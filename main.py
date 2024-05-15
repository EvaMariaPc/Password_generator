from password_manager import PasswordManager
from cryptography.fernet import Fernet


def main():
    try:
        # Example usage
        key = Fernet.generate_key()
        password_manager = PasswordManager(key)

        username = input("Enter your username: ")
        favorite_number = input("Enter your favorite number: ")
        dob = input("Enter your date of birth (YYYY-MM-DD): ")
        age = input("Enter your age: ")
        favorite_color = input("Enter your favorite color: ")
        has_dog = input("Do you have a dog? (yes/no): ").lower() == 'yes'
        dog_name = input("Enter your dog's name: ") if has_dog else ""
        favorite_thing = input("Enter your favorite thing in the world: ")

        password_manager.add_password(username, favorite_number, dob, age, favorite_color, has_dog, dog_name, favorite_thing)
        print("Password added successfully!")

        # Retrieve the generated password
        password = password_manager.get_password(username)
        if password:
            print("Generated Password:", password)
        else:
            print("Username not found.")

    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()
