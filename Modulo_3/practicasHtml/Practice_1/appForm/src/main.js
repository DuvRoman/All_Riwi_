const username = document.getElementById('name')
const lastname = document.getElementById('lastname')
const email = document.getElementById('email')
const password = document.getElementById('password')
const btn = document.getElementById('buttonR')

const userData = [{
  
  userName : "",
  lastName : "",
  userEmail: "",
  userPassword: ""

}];



username.addEventListener('inpunt', (e)=> {
  userData.userName = e.target.value;
  console.log(userData.userName)
})
lastname.addEventListener('inpunt', (e)=> {
   lastName= e.target.value;
})
userEmail.addEventListener('inpunt', (e)=> {
   userEmail= e.target.value;
})
userPassword.addEventListener('inpunt', (e)=> {
   userPassword= e.target.value;
})

btn.addEventListener('click', ()=>{
  localStorage.setItem('name', userName)
  
})

document.querySelector('#app').innerHTML = 

setupCounter(document.querySelector('#counter'))
