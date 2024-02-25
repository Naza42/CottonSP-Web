document.addEventListener('DOMContentLoaded', function() {
  console.log('Script cargado correctamente');

  document.querySelector('#tarjetasCarrusel').addEventListener('click', function(event) {
    console.log('Evento de clic detectado');
    // Puedes mantener el código existente para manejar el clic de los botones
    if (event.target.classList.contains('siguiente')) {
      siguienteTarjeta();
    } else if (event.target.classList.contains('anterior')) {
      anteriorTarjeta();
    }
  });

  // Iniciar el avance automático cada 1 minuto
  setInterval(function() {
    siguienteTarjeta();
  }, 15000);  // 60000 milisegundos = 1 minuto
});

let currentIndex = 0;
const tarjetasWrapper = document.querySelector('.tarjetas-wrapper');
const tarjetas = document.querySelectorAll('.tarjeta');

function mostrarTarjetas(index) {
  const translateValue = -index * 100 + '%';
  tarjetasWrapper.style.transform = 'translateX(' + translateValue + ')';
}

function siguienteTarjeta() {
  if (currentIndex < (tarjetas.length/2) - 1) {
    currentIndex++;
  } else {
    currentIndex = 0;
  }
  mostrarTarjetas(currentIndex);
}

function anteriorTarjeta() {
  if (currentIndex > 0) {
    currentIndex--;
  } else {
    currentIndex = (tarjetas.length/2) - 1;
  }
  mostrarTarjetas(currentIndex);
}