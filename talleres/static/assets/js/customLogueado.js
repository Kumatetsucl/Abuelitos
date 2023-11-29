$(document).ready(function () {
  $("#sidebarCollapse").on("click", function () {
    $("#sidebar").toggleClass("active");
  });
});


function toggleEdicion() {
  var campos = document.querySelectorAll("input, select");
  var botonEditar = document.getElementById("editarBtn");
  var botonEnviar = document.getElementById("BotonEnviar");

  for (var i = 0; i < campos.length; i++) {
    campos[i].disabled = !campos[i].disabled;
  }

  if (botonEditar.innerHTML === "Editar") {
    botonEditar.innerHTML = "Guardar";
    botonEditar.classList.add("disabled");
    botonEditar.hidden = true;
    botonEnviar.classList.add("enabled");
    botonEnviar.hidden = false;
  } else {
    botonEditar.innerHTML = "Editar";
    botonEditar.classList.remove("disabled");
    botonEditar.hidden = false;
    botonEnviar.hidden =true;
  }
}
