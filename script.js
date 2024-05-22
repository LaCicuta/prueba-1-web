const elements = document.querySelectorAll('.warningReq'); //Llama a los mensajes de error
elements.forEach(element => { //Itera en cada uno
    element.hidden=true; //Los oculta    
});

/*Validador de casillas requeridas y formato e datos*/
function checkForm(){
    flag = true;
    const elements = document.querySelectorAll('.warningReq'); //Llama a los label de warning
    elements.forEach(element => {
        const check = document.getElementById(element.getAttribute('for')).value; //Llama a los input de cada label warning
        if(check==""||check==null){ 
            if(element.getAttribute('id')=="msgCorreo"){ 
                element.hidden=true; //Si está vacía no muestra el mensaje de correo erroneo
            }else{
                flag=false;
                element.hidden=false; //Si está vacía muestra el mensaje de error
            }
        } else if(element.getAttribute('id')=="msgCorreo"){
            const re = /.+@[a-z0-9.\-]+\.[a-z]{2,}$/; //Formato de correo correcto
            if(!re.test(check)){
                flag=false;
                element.hidden=false; //Si no cumple el formato muestra mensaje de error
            }
        } else{ element.hidden=true; } //Si no está vacía no muestra el mensaje de error
    });
    return flag; //Regresa true o false según si hay o no errores
}

/*Mostrar modal de envío exitoso*/
document.getElementById('form').addEventListener('submit', function(event){ //Evento de envío
    event.preventDefault(); //Cancela el Submit
    checkForm(); // Comprueba que las casillas estén sin errores
    if(checkForm){
        const modal = new bootstrap.Modal(document.getElementById('formEnviado')); //Instancia de Modal
        modal.show(); //Muestra Modal de envío exitoso
        setTimeout(function(){
            document.getElementById('form').submit();
        }, 3000); //Pasado 3 segundos activa el sumbit
    }
});