// function crearMultiplicador(multiplicador){
//     return function(num){
//         return num * multiplicador
//     }
// }

// const response = crearMultiplicador(2);

// const result =response(4);

// console.log(result)
  let tareas= [{
        'id' : 0,        'content': ""
    }];

    let contador = 0;

document.addEventListener('click', (e)=>{
  

    if(e.target.id === 'button'){
        let getTareas = JSON.parse(localStorage.getItem('tareas')) || [];
        let ultimoIdEnStorage = getTareas.length > 0 ? parseInt(getTareas[getTareas.length - 1].id) : 0;
        tareas.id = ultimoIdEnStorage + contador +1;
        tareas.content= document.getElementById('input').value;
        getTareas.push({...tareas})
        localStorage.setItem('tareas', JSON.stringify(getTareas));
        mostrarTareas();
        alert("Tarea Agregada con Exito ⤵")
    }
})


function mostrarTareas (){
    const lista = document.getElementById("lista");
    const getTareas = JSON.parse(localStorage.getItem('tareas')) || [];

    lista.innerHTML = getTareas.map( tarea=>
            `<li  id="${tarea.id}"class="tarea">
                <span>${tarea.content}</span>
                    <div>
                        <button id="btn_edit"class="btn_1">📝</button>
                        <button id="btn_delete"class="btn_1">❌</button>
                        <span id="state" class = "pendiente">Pendiente</span>
                     </div>
            </li>`
        ).join('');
    }

    function eliminar(id){
        const getTareas = JSON.parse(localStorage.getItem('tareas')) || [];
        let filter = getTareas.filter( d=> d.id != id )
            localStorage.setItem('tareas', JSON.stringify(filter))
            mostrarTareas()
    }

    document.addEventListener('click', (e)=>{
        let btn = e.target.id
        if (btn == "btn_delete") {
            let id = e.target.parentElement.parentElement.id;
            console.log(id)
            eliminar(id)
        }
        })