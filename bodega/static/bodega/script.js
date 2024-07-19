const elements = document.querySelectorAll('.warningReq'); //Llama a los mensajes de error
const msgPassOk = document.getElementById('msgPassOk');
elements.forEach(element => { //Itera en cada uno
    element.hidden=true; //Los oculta    
});
if(msgPassOk){ msgPassOk.hidden=true;};

/*Validador de casillas requeridas y formato e datos*/
function checkForm() {// Validar solicitud de contacto
    let flag = true;
    const elements = document.querySelectorAll('.warningReq');
    elements.forEach(element => {
        const check = document.getElementById(element.getAttribute('for')).value;
        if (check == "" || check == null || check.length < 1) {
            if (element.id == "msgCorreo" || element.id == "msgPass" || element.id == "msgDate" || element.id == "msgPhone") {
                element.hidden = true;
            } else {
                flag = false;
                element.hidden = false;
            }
        } else if (element.getAttribute('id') == "msgCorreo") {
            const re = /.+@[a-z0-9.\-]+\.[a-z]{2,}$/;
            if (!re.test(check)) {
                flag = false;
                element.hidden = false;
            } else {
                element.hidden = true;
            }
        } else if (element.getAttribute('id') == "msgPass") {
            const pass = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*-_=+;:,.<>?/~]).{10,18}$/;
            if (!pass.test(check)) {
                flag = false;
                element.hidden = false;
                document.getElementById('msgPassOk').hidden = true;
            } else {
                element.hidden = true;
                document.getElementById('msgPassOk').hidden = false;
            }
        } else if (element.getAttribute('id') == "msgDate") {
            const date = /^(0[1-9]|[1-2][0-9]|3[0-1])\/(0[1-9]|1[0-2])\/[0-9]{4}$/;
            if (!date.test(check)) {
                flag = false;
                element.hidden = false;
            } else {
                element.hidden = true;
            }
        } else if (element.getAttribute('id') == "msgPhone") {
            const phone = /^\+([0-9]{11})$/;
            if (!phone.test(check)) {
                flag = false;
                element.hidden = false;
            } else {
                element.hidden = true;
            }
        } else if (element.getAttribute('id') == "password2") {
            if (document.getElementById('password').value != document.getElementById('password2').value) {
                flag = false;
                element.hidden = false;
            } else {
                element.hidden = true;
            }
        } else {
            element.hidden = true;
        }
    });

    return flag;
}

/* Mostrar modal de envío exitoso */
const form = document.getElementById('form');
if (form) {
    form.addEventListener('submit', function (event) { // Evento de envío
        event.preventDefault(); // Cancela el Submit
        if (checkForm()) { // Comprueba que las casillas estén sin errores
            const modal = new bootstrap.Modal(document.getElementById('formEnviado')); // Instancia de Modal
            modal.show(); // Muestra Modal de envío exitoso
            setTimeout(function () {
                form.submit();
            }, 3000); // Pasado 3 segundos activa el submit
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



