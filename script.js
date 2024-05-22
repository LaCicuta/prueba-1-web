/*Contacto */
const elements = document.querySelectorAll('.warningReq');
elements.forEach(element => {
    element.hidden=true;    
});

const form = document.getElementById('enviarContacto');
const modal = new bootstrap.Modal(document.getElementById('infoEnviada'));

form.addEventListener('submit', (e) => {
    e.preventDefault();
    if(checkForm){
        modal.show();
        setTimeout(() => {
            form.submit.bind(form)();
        }, 4000); 
    }
});

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
            if(!re.test(check)){
                flag=false;
                element.hidden=false;
            }
        } else{ element.hidden=true; }
    });
    if(flag){
        return true;
    }
    return false;
}