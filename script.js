const elements = document.querySelectorAll('.warningReq'); //Llama a los mensajes de error
const msgPassOk = document.getElementById('msgPassOk');
elements.forEach(element => { //Itera en cada uno
    element.hidden=true; //Los oculta    
});
if(msgPassOk){ msgPassOk.hidden=true;};

/*Validador de casillas requeridas y formato e datos*/
function checkForm(){//Validar solicitud de contacto
    flag = true;
    const elements = document.querySelectorAll('.warningReq');
    elements.forEach(element => {
        const check = document.getElementById(element.getAttribute('for')).value;
        if(check==""||check==null){
            if(element.getAttribute('id')=="msgCorreo"){ 
                element.hidden=true;
            }else{
                flag=false;
                element.hidden=false;
            }
        } else if(element.getAttribute('id')=="msgCorreo"){
            re=/.+@[a-z0-9.\-]+\.[a-z]{2,}$/
            flag = re.test(check);
            element.hidden=re.test(check);
        } else if(element.getAttribute('id')=="msgPass"){
            pass = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*-_=+;:,.<>?/~]).{10,18}$/;
            flag = pass.test(check);
            element.hidden=pass.test(check);
            document.getElementById('msgPassOk').hidden=!pass.test(check);
        } else{ element.hidden=true; }
    });
    if(flag){
        return true;
    }
    return false;
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