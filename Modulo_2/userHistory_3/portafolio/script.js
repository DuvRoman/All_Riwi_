
window.onload = function() {
    alert("¡Bienvenido a mi portafolio! \n Soy Tu desarrollador favorito you know 😉.");
};


const botonEnviar = document.getElementById('btn-enviar');
const section1= document.getElementById('section1');



botonEnviar.addEventListener('click', function(event) {
    event.preventDefault();

    section1.innerText = "¡Gracias por contactarme! He recibido tu mensaje y pronto te responderé.";
    section1.style.color = "#ff0707ff"; 
    section1.style.fontSize= "80px"; 
   

    const formulario = document.querySelector('.formulario1');
    
    if (formulario.style.opacity === '0.5') {
        formulario.style.opacity = '1';
    } else {
        formulario.style.opacity = '0.5'; 
    }
    
    console.log("El botón ha respondido correctamente.");
});