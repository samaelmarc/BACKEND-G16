from flask import Flask
from variables import conexion
from models.usuario import UsuarioModel
from models.direccion import DireccionModel

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


#before_request > se mandara a llamar a esta funcionalidad antes que cualquier request(peticion)
#create.all debe estar dentro de un request
#create_all > crea todas las tablas que no se han creado en la base de datos 
@app.before_request
def inicializacion():
    conexion.create_all()


#creamos un controlador de pruebas
@app.route('/')
def inicial():
    return{
        'message': 'Bienvenido a mi API de usuarios'
    }
if __name__ == '__main__':
    app.run(debug=True)
    