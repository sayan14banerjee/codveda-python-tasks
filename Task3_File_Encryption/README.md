# 🔒 File Encryptor/Decryptor

A Python script that allows you to **encrypt and decrypt files** using **Fernet encryption** from the `cryptography` library. This ensures your files are secure and cannot be read without the key.

---

## 🚀 Features

* Encrypt any file and save it with `.enc` extension
* Decrypt an encrypted file back to original content
* Automatic **key generation** (`key.key`) if it doesn't exist
* Simple **CLI menu** for user-friendly interaction
* Supports all file types: `.txt`, `.pdf`, `.jpg`, etc.
* Decrypted files are saved with prefix `decrypted_` to avoid overwriting original files

---

## 💻 Requirements

* Python 3.x
* `cryptography` module

Install cryptography via pip if not already installed:

```bash
pip install cryptography
📁 Files
file_encryptor.py → Main Python script

key.key → Secret key for encryption/decryption (auto-generated)

Any file you want to encrypt/decrypt (e.g., test.txt)

⚡ Usage
Place file_encryptor.py and the file you want to encrypt/decrypt in the same folder.

Run the script:

bash
Copy code
python file_encryptor.py
Choose an option from the CLI menu:

css
Copy code
1 → Encrypt a file
2 → Decrypt a file
Enter the filename (with extension) when prompted.

🔐 Example
Encrypt test.txt:
mathematica
Copy code
Enter your choice (1/2): 1
Enter the filename: test.txt
Output: test.txt.enc

Decrypt test.txt.enc:
mathematica
Copy code
Enter your choice (1/2): 2
Enter the filename: test.txt.enc
Output: decrypted_test.txt

⚠️ Notes
Keep key.key safe! Without it, encrypted files cannot be decrypted.

Encryption works on all types of files (text, images, PDF, etc.).

Decrypted files are prefixed with decrypted_ to prevent overwriting the original file.

📂 Folder Structure Example
vbnet
Copy code
/FileEncryptionProject
    ├─ file_encryptor.py
    ├─ key.key
    ├─ test.txt
    └─ test.txt.enc
🎥 Video Demo
Watch a sample demo of the script in action:
File Encryptor/Decryptor Demo

🔗 Connect with Me
LinkedIn Profile