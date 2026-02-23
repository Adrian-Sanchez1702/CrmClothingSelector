document.getElementById("btn__registrarse").addEventListener("click", register);
document.getElementById("btn__iniciar-sesion").addEventListener("click", iniciarSesion);

//Declaración de variables
var contenedor__login_registrer = document.querySelector(".contenedor__login-registrer");
var formulario_login = document.querySelector(".formulario__login");
var formulario_register = document.querySelector(".formulario__register");
var caja__trasera_login = document.querySelector(".caja__trasera-login");
var caja__trasera_register = document.querySelector(".caja__trasera-register");

function iniciarSesion(){
    
    formulario_register.style.display = "none";
    contenedor__login_registrer.style.left = "10px";
    formulario_login.style.display = "block";
    caja__trasera_register.style.opacity = "1";
    caja__trasera_login.style.opacity = "0";
    
}

function register(){
    
    formulario_register.style.display = "block";
    contenedor__login_registrer.style.left = "410px";
    formulario_login.style.display = "none";
    caja__trasera_register.style.opacity = "0";
    caja__trasera_login.style.opacity = "1";

}