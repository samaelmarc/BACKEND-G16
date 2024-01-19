from flask import Flask , request
#__name__ > variable de python que sirve para indicar si el archivo que
#estamos utilizando es el archivo principal del proyecto, esto sirve para que la instancia de Flask solamente corra en el archivo principal y asi evitar instancias de Flask ena rchivos secundarios del proyecto
#cada ves que el cliente realize una peticion toda esa informacion se alamcenara en el request


app = Flask(__name__) # encargado de crear mi servidor del backend
# si el archivo es el archivo principal el valor de __name__ sera __main__

#uso de decoradores
#para usar un enpoint, modificamos el comportamiento
#sirve para utilizar un metodo sin la necesidad de modificarlo desde la clase en la cual estamos haciendo la referencia
#GET > devolver
#POST > creaciones
#PUT > Actualizaciones
@app.route('/',methods = [ 'GET', 'POST','PUT'])

#ejemplo
def inicio():
    #request.method > devolvera el metodo HTTP qe esta utilizando el cliente
    if request.method == 'PUT':
        return{
            'message':'Actualizacion exitosa'
        },202 #estado de respuesta http (OK)
    elif request.method == 'GET':
        return{
            'message':'Devolucion exitosa'
        },200 #OK
    elif request.method == 'POST':
        return{
            'message':'Creacion exitosa'
        },201 #CREATED
    print(request.method)
    return{
        'message':'Bienvenido a mi primera API en Flask',
        'content': 'hola'
    }
#asi lenvatamos nuestro servidor de flask
#debug = True activa el debugger para que se actualize sin necesidad de apagar y prender el servidor

app.run(debug=True)