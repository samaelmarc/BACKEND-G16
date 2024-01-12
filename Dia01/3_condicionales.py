#if > si
edad = 30
nacionalidad = 'BRASIL'

if edad > 18 and nacionalidad == 'PERUANO':
    print('puedes votar')
#else > sino
else:
    print('llamare a tus padres')
    
#if > si
edad = 30
nacionalidad = 'BRASIL'

if edad > 18 or nacionalidad == 'PERUANO':
    print('puedes votar')
#else > sino
else:
    print('llamare a tus padres')
    
    
if edad > 18 :
    print('puedes votar')
#elif si no si
elif edad > 15:
    print('Falta poco para votar')
else:
    print('No puedes votar')


#ejercicio
#segun el sexo y la estatura
# si es masculino
    ## si mide mas de 1.50 entonecs indicar que no hay prendas
    #si mide entre 1.30 y 149 indicar que si hay ropa
    # si mide menos de 1.30 indicar que no hay prendas
# si es femenino 
    #si mide mas de 1.40 indicar que no hay prendas
    #so mde entre 1.10 y 1.49 indicar que si hay
    # si mide menos de 1.10 indicar que no hay
    
#tarea  
 

sexo = 'Masculino'
estatura = 1.35
# output > si hay ropa
if sexo == 'Masculino':
    if estatura < 1.50 or estatura < 1.30:
        if estatura >= 130 and estatura <= 1.49:
            print('Si hay ropa')
        else:
            print('No hay prendas')

sexo = 'Masculino'
estatura = 1.80
# output > no hay ropa
if sexo == 'Masculino':
    if estatura < 1.50 or estatura < 1.30:
        if estatura >= 130 and estatura <= 1.49:
            print('Si hay ropa')
        else:
            print('No hay prendas')
    else:
            print('No hay prendas')
sexo = 'Femenino'
estatura = 1.20
#output > si hay ropa
if sexo == 'Femenino':
    if estatura < 1.50 or estatura < 1.30:
        if estatura >= 130 and estatura <= 1.49:
            print('Si hay ropa')
        else:
            print('No hay prendas')
    else:
            print('No hay prendas')
sexo = 'Femenino'
estatura = 1.08
# output > no hay ropa
