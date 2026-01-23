import { refresh } from "./refresh";

const links = {
    "/": "/index.html",
    "/register": "/public/views/register.html",
    "/login": "/public/views/login.html",
    "/homePage" : "/public/views/homePage.html"
};

const userData = [{
  
  userName : "",
  lastName : "",
  userEmail: "",
  userPassword: ""

}];

document.addEventListener('click', async (e) => {

    if (e.target.matches('.data-link')) {
        e.preventDefault();
        const path = e.target.getAttribute('href');
        localStorage.setItem('path', path)
        const file = links[path];

        if (file) {
            const content = await refresh(file);
            window.history.pushState({}, '', '/register'); 
            document.querySelector('#app').innerHTML = content;
        }
    }


    if(e.target.id == "buttonR"){
        userData.userName = document.getElementById('name')?.value.trim();
        userData.lastName = document.getElementById('lastname')?.value.trim();
        userData.userEmail = document.getElementById('email')?.value.trim();
        userData.userPassword = document.getElementById('password')?.value.trim();

        let incompleto = false
            for (let llave in userData) {
                if (userData[llave] === "") {
                incompleto = true;
                break;
                } 
            }
        if(incompleto){
            alert("Datos imcompletos")
            return  
        }
            const getData= JSON.parse(localStorage.getItem('userData'))|| [];
            getData.push({...userData})
            localStorage.setItem('userData', JSON.stringify(getData))
            const ruta = await refresh(links['/login'])
            window.history.pushState({}, '', '/login');  
            document.querySelector('#app').innerHTML = ruta;
            alert("Usuario registrado con exito ✅")         
    }

        const email_1 = document.getElementById('email_1')?.value.trim();
        const pass_1 = document.getElementById('password_1')?.value.trim();
        const getData = JSON.parse(localStorage.getItem('userData')) || [];
        if(e.target.id == 'buttonI' ){

            let revition = getData.find((u) => email_1 === u.userEmail && pass_1 === u.userPassword)

            if(revition){
                const ruta = await refresh(links['/homePage'])
                document.querySelector('#app').innerHTML = ruta;
            }else{
                alert("Credenciales incorrectas 🚫")
                return
            }

        }
});

                









