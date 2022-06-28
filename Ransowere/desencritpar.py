from ast import Return
from cryptography.fernet import Fernet
import os


def cargar_key():
    return open('key.key','rb').read()#esto es para cargar la llaves


def decrypt(items,key):
    f=Fernet(key)
    for item in items:
        with open(item,'rb') as file:#este es para lectura binaria el rb
            encrypted_data=file.read()
        decrypted_data=f.decrypt(encrypted_data)
        with open(item,'wb')as file:
            file.write(decrypted_data)


if __name__ == '__main__':
    path_to_encrypt='D:\Hackear'
    os.remove(path_to_encrypt+'\\'+'readme.txt')

    items =os.listdir(path_to_encrypt)#este enlista los archivos encriptados para decepcritalos
    full_path=[path_to_encrypt +'\\'+item for item in items]

    key=cargar_key()
    decrypt(full_path,key)


#punto importante si quieres desepcritar un archivo tienes que tener mucho cuidado de estar encriptando varias
#veces ya que de ley puedes dañar todos los archivos y no puedes desecriptar todos de una sola vez
