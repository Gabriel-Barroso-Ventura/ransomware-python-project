import os
import pyaes

secret = input("What the secret key?")

if secret == "secretencryptkey":
    for root, dir, files in os.walk("./"):
        for f in files:
            if f != "decrypt.py" and f != "encrypt.py" and f.split(".")[-1] == "ransomware":
                name = os.path.join(root, f)
                
                with open(name, "rb") as file:
                    file_data = file.read()

                key = secret.encode()
                aes = pyaes.AESModeOfOperationCTR(key)

                data_decrypt = aes.decrypt(file_data)

                with open(name, "wb") as file:
                    file.write(data_decrypt)

                new_name = name.strip(".ransomware")
                os.rename(name, f".{new_name}")
else:
    print("Wrong Decrypt Key!")
