console.log('Hola')
//desde el front end vamos a  ingresar productos
const button = document.getElementById('crearProductoBtn')
const nombreProducto = document.getElementById('nombre')
const precioProducto = document.getElementById('precio')
const disponibleProducto = document.getElementById('disponible')
//funcionalidad del botton y input
function crearProducto(e) {
    e.preventDefault()
    const body = {
        nombre : nombreProducto.value,
        precio: +precioProducto.value,
        disponible: disponibleProducto.checked
    }
    crearProductoRequest(body).then((resultado)=>{
        if(resultado === true){
            alert('Producto creado exitosamente')
        }else{
            alert('Error al crear el producto')
        }
    }).catch((e)=>{
        alert(`Error al crear el producto! ${e.message}`)
    })
}

async function crearProductoRequest(body){
    //stringify  convierte el objeto javascryt a un formato string para que lo pueda recibir el back end (jason)
    const solicitud = await fetch('http://127.0.0.1:5000/producto',{method:'POST', body:JSON.stringify(body),headers:{
        //los header sirven para enviar un encabezado de la peticion es decir gracias a estos el backend sabra que informacion recibe, cuestiones de autenticacion , el origen de la peticion entre otros
        'Content-Type':'application/json',
    }})
    return solicitud.status === 201
}   

button.addEventListener('click',crearProducto)

//consumimos nuestro backend
async function pedirProductos(){
    const solicitud = await fetch('http://127.0.0.1:5000/productos')
    console.log(solicitud.status)

    //el text() se utiliza cuando el backend devuelve solamente texto
    //cuando el back end devuelve un diccionario .json
    //console.log(await solicitud.text()) // retorna la informacion sin parsear (sin convertir a un formato legible js)
    //console.log(await solicitud.json())//
    const data = await solicitud.json()//me da  la informacion parseada para JS la puede entender
    console.log(data)
}

pedirProductos()