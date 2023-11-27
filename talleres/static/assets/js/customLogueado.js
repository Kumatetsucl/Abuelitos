$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });
});

function mostrarInfoTaller() {
    var seleccion = document.getElementById("taller").value;

    // Oculta todas las secciones de información
    document.getElementById("infoYoga").classList.add("d-none");
    document.getElementById("infoPintura").classList.add("d-none");
    document.getElementById("infoCeramica").classList.add("d-none");

    // Muestra la sección de información correspondiente al taller seleccionado
    if (seleccion === "yoga") {
      document.getElementById("infoYoga").classList.remove("d-none");
    } else if (seleccion === "pintura") {
      document.getElementById("infoPintura").classList.remove("d-none");
    } else if (seleccion === "ceramica") {
      document.getElementById("infoCeramica").classList.remove("d-none");
    }
  }