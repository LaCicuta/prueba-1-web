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
        if(check==""||check==null||check.lenght < 1){
            if(element.id=="msgCorreo" || element.id=="msgPass" || element.id=="msgDate" || element.id=="msgPhone"){ 
                element.hidden=true;
            }else{
                flag=false;
                element.hidden=false;
            }

        } else if(element.getAttribute('id')=="msgCorreo"){
            re=/.+@[a-z0-9.\-]+\.[a-z]{2,}$/
            element.hidden=re.test(check);
            flag = re.test(check);

        } else if(element.getAttribute('id')=="msgPass"){
            pass = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*-_=+;:,.<>?/~]).{10,18}$/;
            element.hidden=pass.test(check);
            document.getElementById('msgPassOk').hidden=!pass.test(check);
            flag=pass.test(check);

        } else if (element.getAttribute('id') == "msgDate") {
            date= /^(0[1-9]|[1-2][0-9]|3[0-1])\/(0[1-9]|1[0-2])\/[0-9]{4}$/;
            element.hidden = date.test(check);
            flag=date.test(check);

        } else if (element.getAttribute('id') == "msgPhone") {
            phone= /^\+([0-9]{11})$/;
            element.hidden = phone.test(check);
            flag=phone.test(check);
        }

        else{ element.hidden=true; }

    });

    if(flag){
        return true;
    }
    return false;
}

/*Mostrar modal de envío exitoso*/
const form = document.getElementById('form');
if(form){
    form.addEventListener('submit', function(event){ //Evento de envío
        event.preventDefault(); //Cancela el Submit
        checkForm(); // Comprueba que las casillas estén sin errores
        if(checkForm){
            const modal = new bootstrap.Modal(document.getElementById('formEnviado')); //Instancia de Modal
            modal.show(); //Muestra Modal de envío exitoso
            setTimeout(function(){
                document.getElementById('form').submit();
            }, 3000); //Pasado 3 segundos activa el submit
        }
    });
}

/*Desea Cerrar */
const cerrarSesion = document.getElementById('cerrarSesion');
if(cerrarSesion){
    cerrarSesion.addEventListener('click', function(e){
        e.preventDefault();
        const confirmar = window.confirm('¿Cerrar sesión?');
        if (confirmar){
            location.href=cerrarSesion.href;
        }
    });
}



