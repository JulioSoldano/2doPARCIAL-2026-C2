class Cancion
    def __int__(self,id:int,titulo:str,artista:str, album:str, genero:str, anio:int,duracion_seg:int):
        self.id=id
        self.titulo=titulo
        self.artista=artista
        self.album=album
        self.genero=genero
        self.anio=anio
        self.duracion_seg=duracion_seg

    def duracion_mmss(self):
        minutos = self.duracion // 60
        segundos = self.duracion % 60
        return f"{minutos}:{segundos:02d}"

•	__str__ devuelve #12 Jijiji | Patricio Rey y sus Redonditos de Ricota | 1988 | 5:16.
•	__eq__ compara por id.

def __str__(self):
        return f"{self.id} |({self.artista})| ({self.anio}| ({self.duracion_seg}


#Teoría. La duración se guarda en segundos enteros y duracion_mmss la calcula. 
#Explicar en dos oraciones por qué conviene guardarla así y no en un string "5:16".
#Rta: Porque en formato string seria complicado poder hacer calculos con los numeros,
# ya que habria que transformar el string en int, ya que es mayor el procesamiento que se debe realizar
#en la conversión. Es mas simple dividir el total de segundos en minutos (y su resto) que la transformacion de datos.
________________________________________      
        