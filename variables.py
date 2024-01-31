from flask_sqlalchemy import SQLAlchemy

#La conexion entre mi ORM y mi base de datos
# No se recomienda tener masd e 1 conexion a la base de datos
conexion = SQLAlchemy()
