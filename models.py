import db
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime

class Tarea(db.Base):
    '''clase Tarea
    Almacena las tareas completadas y las guarda en la db  tareas
    hecha: booleano que marca si la tarea se ha completado o no.
    args:
    id: se crea automáticamante de forma incremental
    contenido: string de máximo 200 caracteres en el que se indica el contenido de la tarea'''
    __tablename__ = "tarea"
    id = Column(Integer, primary_key=True) # Automaticamente esta PK se convertirá en SERIAL (AUTOINCREMENT)
    contenido = Column(String(200), nullable=False)
    categoria = Column(String(200))
    fecha_limite= Column(DateTime, nullable=False)
    hecha = Column(Boolean)
    def __init__(self, contenido, categoria, fecha_limite, hecha=False):
        '''constructor de la CLASE TAREA'''
        self.contenido = contenido
        self.categoria=categoria
        self.fecha_limite=fecha_limite
        self.hecha=hecha
        print("Tarea creada con éxito", self.fecha_limite)

    def __str__(self):
        '''metodo str de la clase tarea'''
        return "Tarea {}: {}, ({}), {}".format(self.id, self.contenido, self.hecha, self.fecha_limite)
