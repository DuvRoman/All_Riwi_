  
   
    
   


export async function getWeather(city) {

     const apiKey = "4f2ce25643b7e741ae371a663e6a9494"

     let url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}`
    try {
        const  response = await fetch(url) 
        const  data = response.json()
        return data
    } catch (error) {
        console.error(error);
    }
}  

 



// vcomo hago para vincular un spa en vite con peticion fetch, con un navbar en una pagina principal que me cambie el contenido despues de darle click a un link del navbar