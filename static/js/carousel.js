const tarjetasWrapper = document.querySelector('.tarjetas-wrapper');
let intervalo;
let currentIndex = 0;
let tarjetas = document.querySelectorAll('.test');
let tarjetasVisibles = window.innerWidth <= 768 ? 1 : 3;

function iniciarAvanceAutomatico() {
  intervalo = setInterval(function() {
    siguienteTarjeta();
  }, 5000);
}
function reiniciarAvanceAutomatico() {
  clearInterval(intervalo); 
  iniciarAvanceAutomatico(); 
}
function mostrarTarjetas(index) {
  const translateValue = -index * 100 + '%';
  tarjetasWrapper.style.transform = 'translateX(' + translateValue + ')';
}
function siguienteTarjeta() {
  const target = window.innerWidth <= 768 ? tarjetas.length - 1 : tarjetas.length%tarjetasVisibles;
  const isNotEndCarousel =window.innerWidth <= 768 ? currentIndex < target : currentIndex <= target;
  if (isNotEndCarousel) {
    currentIndex++;
  } else {
    currentIndex = 0;
  }
  mostrarTarjetas(currentIndex);
}
function anteriorTarjeta() {
  const target = window.innerWidth <= 768 ? tarjetas.length - tarjetasVisibles : tarjetas.length%tarjetasVisibles  + 1;
  if (currentIndex != 0) {
    currentIndex--;
  } else {
    currentIndex = target;
  }
  mostrarTarjetas(currentIndex);
}

document.querySelector('#tarjetasCarrusel').addEventListener('click', function(event) {
  tarjetas = document.querySelectorAll('.test');
  reiniciarAvanceAutomatico();
  if (event.target.classList.contains('siguiente')) {
    siguienteTarjeta();
  } else if (event.target.classList.contains('anterior')) {
    anteriorTarjeta();
  }
});
window.addEventListener('resize', function() {
  currentIndex = 0
  tarjetasVisibles = window.innerWidth <= 768 ? 1 : 3;
  mostrarTarjetas(currentIndex)
  reiniciarAvanceAutomatico();
});

iniciarAvanceAutomatico();