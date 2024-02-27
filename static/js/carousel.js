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
  console.log("Start")
  siguienteTarjeta();
  }, 15000);  // 60000 milisegundos = 1 minuto

let currentIndex = 0;
const tarjetasWrapper = document.querySelector('.tarjetas-wrapper');
const tarjetas = document.querySelectorAll('.tarjeta');

function mostrarTarjetas(index) {
const translateValue = -index * 100 + '%';
tarjetasWrapper.style.transform = 'translateX(' + translateValue + ')';
}

function siguienteTarjeta() {
const tarjetasVisibles = window.innerWidth <= 768 ? 11 : 3; // Ajusta según tus necesidades
if (currentIndex < tarjetasVisibles) {
  currentIndex++;
} else {
  currentIndex = 0;
}
mostrarTarjetas(currentIndex);
}

function anteriorTarjeta() {
const tarjetasVisibles = window.innerWidth <= 768 ? 1 : 3; // Ajusta según tus necesidades
if (currentIndex > 0) {
  currentIndex--;
} else {
  currentIndex = tarjetasVisibles;
}
mostrarTarjetas(currentIndex);
}