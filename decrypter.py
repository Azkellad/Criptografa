import os
import pyaes

# DESCRIPTAR O ARQUIVO TXT
arquivo_nome = "arquivo.txt.ransomwaretroll"
arquivo = open(arquivo_nome, "rb")
file_data = arquivo.read()
arquivo.close()

#CHAVE DE DESCRIPTAÇÃO
key = b"0123456789abcdef0123456789abcdef"
aes = pyaes.AESModeOfOperationCTR(key)
decrypted_data = aes.decrypt(file_data)

#REMOVE O ARQUIVO CRIPTADO
os.remove(arquivo_nome)

#CRIAR UM NOVO ARQUIVO TXT COM O CONTEÚDO DESCRIPTO
arquivo_novo = open("arquivo.txt", "wb")
arquivo_novo.write(decrypted_data)
arquivo_novo.close()