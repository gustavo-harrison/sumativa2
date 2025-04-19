// ------------------------------ FUNCIÓN FORMULARIO DE CONTACTO -------------------------- //

function validarformulariocontacto(){

    const nombre = document.getElementById("nombre").value.trim();
    const correo = document.getElementById("correo").value.trim();
    const telefono = document.getElementById("telefono").value.trim();
    const edad = document.getElementById("edad").value.trim();
    const mensaje = document.getElementById("mensaje").value.trim();

    if(!nombre || !correo || !telefono || !edad || !mensaje){
        alert("Por favor, ingrese todos los campos seleccionados");
        return;
    }

    if(isNaN(edad) || Number(edad) <= 0){
        alert("Por favor, ingrese una edad valida");
        return;
    } 

    const correoexpre = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if(!correoexpre.test(correo)){
        alert("Por favor, ingrese un correo valido");
        return;
    }

    console.log("Datos del formulario: ");
    console.log(nombre);
    console.log(correo);
    console.log(telefono);
    console.log(edad);
    console.log(mensaje);

}

// ------------------------------ FUNCIÓN REGISTRO FORMULARIO -------------------------- //

function datosformulario() {

    const rut = document.getElementById("rut").value.trim();
    const nombre = document.getElementById("nombre").value.trim();
    const apellidoP = document.getElementById("apellidoP").value.trim();
    const apellidoM = document.getElementById("apellidoM").value.trim();
    const direccion = document.getElementById("direccion").value.trim();
    const comuna = document.getElementById("comuna").value.trim();
    const telefono = document.getElementById("telefono").value.trim();
    const correo = document.getElementById("correo").value.trim();
    const region = document.getElementById("region").value.trim();
    const contrasena = document.getElementById("contrasena").value.trim();

    if (!rut || !nombre || !apellidoP || !apellidoM || !direccion || !comuna || !telefono || !correo || !region || !contrasena) {
        alert("Por favor, ingrese todos los campos seleccionados");
        return;
    }

    if (!validarRut()) {
        return; 
    }
    if (!validarTelefono()) {
        return; 
    }

    if (!validarContrasena()) {
        return; 
    }

    const datosFormulario = {
        rut,
        nombre,
        apellidoP,
        apellidoM,
        direccion,
        comuna,
        telefono,
        correo,
        region,
        contrasena
    };

    localStorage.setItem("datosFormulario", JSON.stringify(datosFormulario));

    console.log("Datos del formulario almacenados en localStorage: ");
    console.log(datosFormulario);
    alert("Los datos han sido ingresados correctamente");
}


// ------------------------------ FUNCIÓN INICIO DE SESIÓN -------------------------- //

function inicioSesion() {

    const rutIngresado = document.getElementById("rut").value.trim();
    const contrasenaIngresada = document.getElementById("contrasena").value.trim();
    const datosFormulario = JSON.parse(localStorage.getItem("datosFormulario"));

    if (!datosFormulario) {
        alert("Usuario no se encuentra en nuestros registros");
        return;
    }

    if (rutIngresado === datosFormulario.rut && contrasenaIngresada === datosFormulario.contrasena) {
        window.location.href = "menu_principal.html";
    } else {
        alert("ERROR");
    }
}

// ------------------------------ VALIDACIONES -------------------------- //

function validarRut() {
    const rut = document.getElementById("rut").value;
    const rutValido = /^([0-9]{1,8})-([0-9kK]{1})$/.test(rut);
    let errorMensaje = document.getElementById("error-rut");

    if (!rutValido) {
        errorMensaje.textContent = "Formato inválido. Ejemplo: 18604555-K";
        return false;  
    } else {
        errorMensaje.textContent = "";
        return true;  
    }
}

// ------

function validarTelefono() {
    const telefono = document.getElementById("telefono").value;
    const telefonoValido = /^\+\d{11}$/.test(telefono);
    let errorMensaje = document.getElementById("error-telefono");

    if (!telefonoValido) {
        errorMensaje.textContent = "Formato inválido. Ejemplo: +56912345678";
        return false;  
    } else {
        errorMensaje.textContent = "";
        return true;  
    }
}

//-----

function validarContrasena() {
    const contrasena = document.getElementById("contrasena").value;
    const contrasenaValida = /^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]{8,}$/.test(contrasena);
    let errorMensaje = document.getElementById("error-contrasena");

    if (!contrasenaValida) {
        errorMensaje.textContent = "La contraseña debe tener al menos 8 caracteres y ser alfanumérica.";
        return false;  
    } else {
        errorMensaje.textContent = "";
        return true;  
    }
}
