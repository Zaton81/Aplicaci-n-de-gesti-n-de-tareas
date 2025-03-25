from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Define la clase para la tabla de administración de la base de datos
class Admin(Base):
    __tablename__ = 'admin'

    id = Column(Integer, primary_key=True, autoincrement=True)
    lista_usuarios = Column(String, nullable=False)
    lista_donaciones = Column(Integer, nullable=False)

    def __int__(self, lista_usuarios=None, lista_donaciones=None):
        self.lista_usuarios = lista_usuarios
        self.lista_donaciones = lista_donaciones

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(20), nullable=False)
    apellido = Column(String(20), nullable=False)
    direccion = Column(String(50), nullable=False)
    localidad = Column(String(50), nullable=False)
    pais = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    telefono = Column(Integer(), nullable=False)
    edad = Column(Integer, nullable=False)
    pasword = Column(String(128), nullable=False)  # Se ha añadido el campo de la contraseña

    def __init__(self, nombre=None, apellido=None, direccion=None, localidad=None, pais=None, email=None, telefono=None,
                 edad=None, pasword=None):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.localidad = localidad
        self.pais = pais
        self.email = email
        self.telefono = telefono
        self.edad = edad
        self.pasword = pasword


class Donacion(Base):
    __tablename__ = 'donaciones_libros'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    localidad = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    titulo = Column(String(100), nullable=False)
    autor = Column(String(50), nullable=False)
    genero = Column(String(50), nullable=False)
    idioma = Column(String(50), nullable=False)
    edicion = Column(Date, nullable=False)

    def __init__(self, nombre=None, localidad=None, email=None, titulo=None, autor=None, genero=None, idioma=None, edicion=None):
        self.nombre = nombre
        self.localidad = localidad
        self.email = email
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.idioma = idioma
        self.edicion = edicion

# Configura la conexión a la base de datos SQLite
engine = create_engine('sqlite:///database/datos.db')

# Crea todas las tablas definidas en las clases de SQLAlchemy
Base.metadata.create_all(engine)

# Crea una sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)
session = Session()