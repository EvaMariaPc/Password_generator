import string
import random
from cryptography.fernet import Fernet


class PasswordManager:
    def __init__(self, key):
        self.key = key
        self.cipher = Fernet(key)
        self.passwords = {}
        self.random_words = ['apple', 'banana', 'cherry', 'dragon', 'elephant', 'frog', 'giraffe', 'horse', 'iguana', 'jaguar']

    def encrypt(self, data):
        return self.cipher.encrypt(data.encode())

    def decrypt(self, data):
        return self.cipher.decrypt(data).decode()

    def generate_password(self, length=12, avoid=[]):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''
        while True:
            password = random.choice(self.random_words) + ''.join(random.choice(characters) for _ in range(length - 6))
            if (len(password) >= 8 and
                any(char.isdigit() for char in password) and
                any(char.isupper() for char in password) and
                sum(char in string.punctuation for char in password) == 1 and
                not any(str(num) in password for num in avoid)):
                break
        return password

    def add_password(self, username, favorite_number, dob, age, favorite_color, has_dog, dog_name, favorite_thing):
        avoid_numbers = [favorite_number, dob, str(age)]
        avoid_words = [favorite_color.lower(), favorite_thing.lower()]
        if has_dog and dog_name:
            avoid_words.append(dog_name.lower())
        password = self.generate_password(avoid=avoid_numbers + avoid_words)
        encrypted_password = self.encrypt(password)
        self.passwords[username] = {
            'password': encrypted_password
        }

    def get_password(self, username):
        if username in self.passwords:
            encrypted_password = self.passwords[username]['password']
            password = self.decrypt(encrypted_password)
            return password
        else:
            return None
