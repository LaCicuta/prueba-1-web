/*Contacto */
const elements = document.querySelectorAll('.warningReq');
elements.forEach(element => {
    element.hidden=true;    
});

document.getElementById('form').addEventListener('submit', function(event){
    event.preventDefault();
    checkForm();
    if(checkForm){
        const modal = new bootstrap.Modal(document.getElementById('formEnviado'));
        modal.show();
        setTimeout(function(){
            document.getElementById('form').submit();
        }, 3000); 
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
            const re = /.+@[a-z0-9.\-]+\.[a-z]{2,}$/;
            if(!re.test(check)){
                flag=false;
                element.hidden=false;
            }
        } else{ element.hidden=true; }
    });
    return flag;
}

