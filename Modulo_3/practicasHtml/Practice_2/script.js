const boton= document.getElementById("myBoton");
const caja= document.getElementById("caja");

let contador= 0

boton.addEventListener('click', () =>{
   console.log("boton presionado");
   contador ++
   caja.innerHTML = `<h2> boton presionado ${contador} <h2/> `
});

let lista = [ usuario1 = {
        "libro" : "Harry potter" ,
        "calificación" : "4.5"
    },
    usuario2={
        "libro" : "Spiderman" ,
        "calificación" : "5"
} ]