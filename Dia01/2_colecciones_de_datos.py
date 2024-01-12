# Podemos agrupar varios valores en una variable

#LISTAS
# Se pueden agrupar modificar, es ordenada ( maneja indices)
alumnos = ['Victor','Hiroito','Marco','Samael','angel','Bryan','Claudia']
#Las listas empiezan con la posicion 0
print(alumnos[0])
print(alumnos[4])

#para saber el contenido(longitud) de datos
print(len(alumnos))
#si queremos recorrer la lista de derecha a izquierda utiliza numeros negativos
print(alumnos[-1])
#otra forma de obtener un elementos de la lista
print(alumnos[len(alumnos)-1])
#agregar elementos a la lista creada
alumnos.append('Franklin')
print(alumnos)
#remover un elemento de la lista lo podemos guardar en una variable
alumno_eliminado = alumnos.pop(3)
print(alumnos)
print(alumno_eliminado)

#del > podemos eliminar variables, eliminar posiciones de la lista y otras cosas
del alumnos[0]
#cada vez que se elimina una posicion de la lista, todas las demas posiciones ocupan ese lugar disponible
print(alumnos)

#modificar el valor de una posicion de una lista
alumnos[0] = 'eduardo'
#limpiamos toda la lista y la dejamos vacia
alumnos.clear()
print(alumnos)

#las listas pueden contener varios tipos de datos
mixto = ['Lunes',10,False,80.5,[1,2,3]]
#ejercicios
ejercicio = [1,2,3,[4,5,6]]
#devolver el valor de 3
#devolver el valor de 5
print(ejercicio[2])
print(ejercicio[3][1])
#TUPLAS
#No se puede modificar y es ordenada (indices)
#Se usa para guardar valores que hamas vana  poder cambiar
#No se puede cambiar, eliminar,agregar
meses = ('enero','Febrero','Marzo','Abril')
print(meses[0])
#control+k+c comentar , control+k+u descomentar
data = ('juan','roberto',[1,2,3,['eduardo','frank']])
#obtener eduardo
print(data[2][3][0])
#set conjuntos
#desornada y modificada
colores = {'negro','blanco','guinda','violeta'}

print(colores)
colores.add('azul')
print(colores)

print('verde' in colores) #False > no esta contenida
colores.remove('blanco')
#diccionarios
#ordenados pero  por llaves y modificables
persona = {
    'nombre':'Eduardo',
    'edad':31,
    'nacionalidad':'peruano',
    'apellido': 'De rivero'
}
print(persona.keys()) #LLAVES
print(persona.values()) # VALORES
print(persona['edad'])
# print(persona['edades']) # JAVASCRIPT SI NO ESTIXTE ME RETORNA UNDEFINED, aca lanza error

persona['nombre'] = 'Juancito'
persona['calzado'] = 'zapatos' # si la llave no existe, entonces la creara

#-------
persona = {
    'nombre':"Roberto",
    'edad': 40,
    'hobbies': ['Nada', 'Pescar', 'Jugar videojuegos'],
    'idiomas': [
        {
            'nombre': 'Ingles',
            'nivel': 'Intermedio'
        },
        {
            'nombre': 'Frances',
            'nivel': 'Basico'
        }
    ],
    'habilidades': {'Puntual', 'Economico', 'Proactivo'},
    'debilidades': ('Mentiroso', 'Resentido', 'Comelon')
}
#darme la edad
print(persona['edad'])
#mostrar los hobbies
print(persona['hobbies'])
#mostrar el ultimo hobbie ingresdo
print(persona['hobbies'][-1])
#Mostrar los idiomas solo sus nombres
print(persona['idiomas'][0]['nombre'])
print(persona['idiomas'][1]['nombre'])
#ver si es proactivo
print('Proactivo' in persona['habilidades'])
#ver cuantas debilidades tiene(cantidad)
print(len(persona['debilidades']))
