#creamos una api
from flask import Flask, request
from uuid import uuid4
from flask_cors import CORS
#app = Flask(__name__) primeros se declara  y luego se trabaja todo por debajo
app = Flask(__name__)



#para configurar mis  CORS lo hago  de la siguiente manera
#si lo dejamos sin ninguna configuracion adicional, va permitir que todos los origenes, todos los metodos y los header sean permitidos
#CORS(app=app)
CORS(app=app, 
     methods = ['GET','POST','PUT','DELETE'], #que metodos pueden acceder a mi API
     #si queremos que se conecte deesde cualquier origen se pone *
     origins=['http://localhost:5500','http://127.0.0.1:5500'], # desde que dominios pueden acceder a mi  API
      #si queremos que se conecte deesde cualquier origen se pone *
     allow_headers=['accept','authorization','content-type'] #que cabeceras ( header) pueden enviar a mi API
     )

#uuid  (uuid4 , el 4 significa la longitud hexadecimales) genera un numero aletario y lo pone como identificador (id)
#0 - 9 , A - F
productos = [
    {
        'id': uuid4(),
        'nombre': 'Palta fuerte',
        'precio': 7.50,
        'disponibilidad': True
             
    },
    {
        'id': uuid4(),
        'nombre': 'Lechuga Carola',
        'precio': 1.50,
        'disponibilidad': True
    }
]

#creamos el primera ( ruta) endpoint
@app.route('/', methods = ['GET'])
def inicio():
    return{
        'message' : 'Bibenvenido a la API productos'
    },200
# creamos la segunda ruta ( api)
@app.route('/productos', methods = ['GET'])
def gestionProductos():
    return {
        'message':'Los productos son',
        'content': productos
    },200
#si voy a recibir un parametro dinamico (que va a cambiar su valor) y eso lo voy a manejar internamente
#los formatos que pueden parsear datos son string int uuid path (son string pero tbm aceptan slashes /)
# al colocar un parseador, si el formato que me envia el cliente no cumple con esta conversion no aceptara la peticion
#si defino unparametro dinamico ese parametro lo tengo que recibir en la funcion def gestionProducto(id): 
#mostramos solo un producto y no todo el contenido
@app.route('/producto/<uuid:id>' , methods = ['GET'])
def gestionProducto(id):
    print(id)
    #tenemos una lista de productos en el cual  en cada posicion tenemos un diccionario y una llave llamada id
    #iteren esos productos y vean si existe el producto con determinado id
    #si no existe entonces retornar un menssage que diga 'Producto no existe' con estado 404
    #pista: hacer un for con if y else dentro de el
    
    for producto in productos:
        if producto['id'] == id:
            return {
                'content': producto
            },200
            
    return {
        'message':'El producto no existe'
    },404
#metodo
#nota: tener cuidado con las rutas
@app.route('/producto' , methods=['POST'])
def crearProducto():
    #convierte la data del body a un diccionary si el body es un JSON
    data =request.get_json()
    #Antes de guardar la informacion en  los productor agregarle el id uuid
    data['id'] = uuid4() # agregamos un campo nuevo
    productos.append(data)
    return{
        'message':'Producto creado exitosamente',
        'content': data
    },201 #created

if __name__ == '__main__':
    app.run(debug=True)
    
