import time

from django.template import Engine
resultado = ""

for i in range(1,10):
    resultado += str(i)

    archivo = open('Virus'+resultado+'.txt', 'w')
    
    
Engine.runAndWait()

resultado = ""
def escritura(dato1, dato2, dato3, dato4, dato5):
      archivo = open('Virus'+resultado+'.txt', 'w')
      archivo.write(dato1)
      archivo.write(dato2)
      archivo.write(dato3)
      archivo.write(dato4)
      archivo.write(dato5)
   
escritura("\rhola mundo bonito","\rhola dos","\rhola ","\rque tal amigos","\rque hay de nuevo viejo")
resultado = ""

for i in range(1, 10):
        resultado += str(i)

        archivo = open('Virus'+resultado+'.docx', 'w')
        escritura("\rhola soy un tipo de virus especial para mantenerte ocupado "
        ,"\rMe encanta hacer que la gente me descargue y despues me borren",
        "\rCon muchas ganas y lastima me tienes que borrrar pero algo tienes que saber de mi ",
        "\rEsto es algo  sencillo pero si hubiera deseado pondria hacer 1000 o 200000 o 300000000000000 de archivos",
        "\rSolo con el afan de hacer que tu disco duro se llene y se sature por no tener espacio asi que trata me bien para la proxima")