const toggleMobileNav = () => {
  const navbar = document.querySelector('#navbar');
  const navToggle = document.querySelector('.mobile-nav-toggle');

  navbar.classList.toggle('navbar-mobile');
  navToggle.classList.toggle('bi-list');
  navToggle.classList.toggle('bi-x');
};

// Activar el toggle al hacer clic en el botón
document.querySelector('.mobile-nav-toggle').addEventListener('click', toggleMobileNav);

// Función para detectar el tamaño de la pantalla y ocultar el menú si es mayor a 768px
const handleResize = () => {
  if (window.innerWidth > 768) {
    document.querySelector('#navbar').classList.remove('navbar-mobile');
  }
};

// Añadir un listener para el resize del navegador
window.addEventListener('resize', handleResize);