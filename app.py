from flask import Flask
from variables import conexion
app = Flask(__name__)
#print(app.config)

#app.config almacenara todas las variables que se utilizara en el proyecto de flask
#Nota no confundir con las variables de entorno!
#ahora agregamos una nueva llave a nuestra variables de configuracion
#dialecto://usuario:contraseña@host:puerto/base_de_datos
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@localhost:3306/alumnos'
#inicializamos la conexion a nuestra BD
# al momentod e pasarle la aplicacion de flask en esta encontraras la cadena de conexion a la BD

conexion.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
    