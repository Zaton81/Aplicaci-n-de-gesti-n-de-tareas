from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#crear motor
engine=create_engine("sqlite:///database/tareas.db",
                     connect_args={"check_same_thread": False} ) #esta línea
#creamos la sesion
Session=sessionmaker(bind=engine)
session=Session()

#instruccion para poder realizar la BS

Base = declarative_base()