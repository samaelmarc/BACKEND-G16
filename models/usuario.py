from sqlalchemy import Column, types
# Si queremos utilizr un tipod e dato en especial para und eerminado motor de base de datos
# from sqlalchemy.dialects.postgresql.types import MONEY
from variables import conexion

# Para indicar que esta clase sera una tabla en la base de datos utilizamos la conexion a la base de datos

class UsuarioModel(conexion.Model):
    id = Column(name='id', 
                type_=types.Integer, 
                autoincrement=True,
                primary_key = True)
    #Si no colocamos el parametro name entonces el nombre de la columna sera el mismo qe el nombre del atributo
    # nullable > puede admitir valores nuilos o no , su valor por defecto es True
    nombre = Column(type_=types.String(100),nullable=False)
    apellido = Column(type_=types.String(100))
    fechaNacimiento = Column(name='fecha_nacimiento',type_=types.Date)
    correo = Column(type_= types.String(100), unique=True)
    
    #Ahora para indicar como queremos que se llame esta tabla en la bd
    
    __tablename__= 'usuarios'
    
    