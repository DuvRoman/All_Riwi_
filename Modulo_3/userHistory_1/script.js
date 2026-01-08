let name_;
let age;

alert("Bienvenido al programa inventado para darte un saludo cordial")

do {

    name_= prompt("Ingrese su nombre:  ");
    age= prompt("Ingrese su edad:  ");

    if( !isNaN(name_) || name_.trim() === "" ){
        alert("Datos del nombre erroneos. Debe de ingresar solo letras en este campo")
        console.error("Numeros o vacios detectados en lugar de letras")

    }else if( isNaN(age) || age.trim() === "" ){
        alert("Datos de la edad erroneos. Debe de ingresar solo numeros en este campo")
        console.error("Letras o vacios detectados en lugar de numeros")
    }
    
} while (!isNaN(name_) || name_.trim() === "" || isNaN(age) || age.trim() === "" );


if(age < 18){
    alert(`Hola ${name_}, eres menor de edad. ¡Sigue aprendiendo y disfrutando del código!`);
}else{
    alert(`Hola ${name_}, eres mayor de edad.  ¡Prepárate para grandes oportunidades en el mundo de la programación!`);
}