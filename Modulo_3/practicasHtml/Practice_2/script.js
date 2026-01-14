import {getWeather}   from "./weather.js";


const boton= document.getElementById("button");
const input= document.getElementById("input");
const content= document.getElementById("contenedor");




boton.addEventListener('click', async () => {
    const data = await getWeather(input.value);
    
    if (data && data.main) {
        content.innerHTML = `${data.main.temp}°C`;
    } else {
        content.innerHTML = "Ciudad no encontrada";
    }
});



