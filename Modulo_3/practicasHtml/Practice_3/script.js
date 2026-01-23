
  let tareas= [{
        'id' : 0,
        'content': ""
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
        document.getElementById('input').value = ""
        mostrarTareas();
        alert("Tarea Agregada con Exito ⤵")
    }
})


function mostrarTareas (contenido = null){
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

function editar(id, content){
    const getTareas = JSON.parse(localStorage.getItem('tareas')) || [];
    let verification = getTareas.find(tarea => tarea.id == id)
    
    if(verification){
        let maping = getTareas.map(cont => cont.content = content )
        localStorage.setItem('tareas', JSON.stringify(maping))
    }else{
        alert("Usuario no encontrado")
    }
   
}

       document.addEventListener('click', (e)=>{
        let btn = e.target.id
        console.log(btn)
        

        if (btn == "btn_delete") {
            let id = e.target.parentElement.parentElement.id;
            console.log(id)
            eliminar(id)
        }else if(btn == "btn_edit"){
            let id_2= e.target.parentElement.parentElement.id;
            const article_2 = document.getElementById('article_2')
            article_2.innerHTML = `<section id="edit" class="edit">
                            <input type="text" placeholder="Edita el texto">
                            <article class="article_edit">
                                <button id="edit_button" class="btn_editor">Editar</button>
                                <button id="edit_cancel" class="btn_editor">Cancelar</button>
                            </article>
                             </section>`
            
            console.log(id_2)
        }
        })

        