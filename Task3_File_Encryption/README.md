# 🎯 File Encryptor/Decryptor

A Python command-line application to **encrypt and decrypt files** securely using **Fernet symmetric encryption**. Users can **encrypt any file** and later **decrypt it** using the same secret key. This ensures that files are safe from unauthorized access.

---

## 🚀 Features

* Encrypt any file and save it with `.enc` extension.
* Decrypt encrypted files back to their original content.
* Automatic **key generation** (`key.key`) if it doesn't exist.
* Menu-based Command Line Interface (CLI) for easy usage.
* Supports all file types: `.txt`, `.pdf`, `.jpg`, etc.
* Decrypted files are saved with prefix `decrypted_` to avoid overwriting original files.
* Error handling for invalid files or wrong keys.

---

## 📂 Project Structure

\`\`\`
FileEncryptionProject/
│── file_encryptor.py    # Main script
│── key.key             # Secret key for encryption/decryption
│── test.txt            # Sample file to encrypt/decrypt
│── README.md           # Documentation
\`\`\`

---

## 🖥️ How to Run

1. Clone this repository or download the folder.
2. Make sure Python 3.x is installed.
3. Install the required library: `cryptography`
4. Open a terminal in the project folder and run `python file_encryptor.py`.
5. Follow the CLI menu:
   * Enter `1` to Encrypt a file
   * Enter `2` to Decrypt a file
6. Enter the filename (with extension) when prompted.

---

## 🎥 Demo

Watch a demo of the script in action:
[File Encryptor/Decryptor Demo](https://youtu.be/your-demo-link)

---

## 📌 Example Usage

**Encrypt `test.txt`:**

\`\`\`
===== File Encryptor/Decryptor =====
1. Encrypt a file
2. Decrypt a file
Enter your choice (1/2): 1
Enter the filename (with extension): test.txt
File encrypted successfully! Saved as test.txt.enc
\`\`\`

**Decrypt `test.txt.enc`:**

\`\`\`
===== File Encryptor/Decryptor =====
1. Encrypt a file
2. Decrypt a file
Enter your choice (1/2): 2
Enter the filename (with extension): test.txt.enc
File decrypted successfully! Saved as decrypted_test.txt
\`\`\`

---

## 🛠️ Technologies Used

* Python 3
* `cryptography` module (`Fernet` for encryption/decryption)
* `os` module (file handling)

---

## 👨‍💻 Author

* Internship Task for **Codveda Technology**
* Created by: *Sayan Banerjee*

---

## 🔗 LinkedIn Submission

Add your LinkedIn post after submission:
[LinkedIn Post](https://www.linkedin.com/in/your-linkedin-profile)
Suggested hashtags: `#CodvedaJourney #CodvedaExperience #FutureWithCodveda`

---
