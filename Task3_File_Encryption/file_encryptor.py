from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    if not os.path.exists("key.key"):
        return generate_key()
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key

def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    encrypted_data = fernet.encrypt(data)
    enc_filename = filename + ".enc"
    with open(enc_filename, "wb") as file:
        file.write(encrypted_data)

    print(f"File encrypted successfully! Saved as {enc_filename}")

def decrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    if filename.endswith(".enc"):
        orig_filename = "decrypted_" + filename[:-4] 
    else:
        orig_filename = "decrypted_" + filename 

    with open(orig_filename, "wb") as file:
        file.write(decrypted_data)

    print(f"File decrypted successfully! Saved as {orig_filename}")

def main():
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    choice = input("Enter 1 or 2: ")
    
    filename = input("Enter filename: ")
    
    if choice == "1":
        encrypt_file(filename)
    elif choice == "2":
        decrypt_file(filename)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()