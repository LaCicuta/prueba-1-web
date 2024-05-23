/*Fecha y hora*/
$(document).ready(function(){
    const fecha = Date.now();
    const hoy = new Date(fecha);
    const options = { year: 'numeric', month: 'long', day: 'numeric'}; //Formato de fecha
    $("#fecha").append(hoy.toLocaleDateString('es-CL', options));
});

/*Hora*/
$(document).ready(function(){
    setInterval(function() {
        const now = new Date();
        const time = now.toLocaleTimeString('es-CL', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
        $("#hora").text(time);
    }, 100);
});

/*Consumo API de finanzas*/
$(document).ready(function(){
    const moneda = new Intl.NumberFormat('es-CL', {style: 'currency', currency: 'CLP', maximumFractionDigits: 3});
    $.get("https://mindicador.cl/api", function(data) { //API de finanzas
        $("#uf").append("UF: "+moneda.format(data.uf.valor));
        $("#dolar").append("Dolar: "+moneda.format(data.dolar.valor));
        $("#euro").append("Euro: "+moneda.format(data.euro.valor));
    }).fail(function() {
        console.log('Error. No se ha podido conectar a la API');
    });
});
