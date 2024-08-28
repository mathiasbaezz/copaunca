const hamburger = document.querySelector(".hamburger");

hamburger.addEventListener('click', () => {
  const navbar = document.getElementById("navbar");
  navbar.classList.toggle("open");

  hamburger.classList.toggle("toggle");

  const isNavbarOpen = navbar.classList.contains("open");
  const navLink = document.querySelectorAll(".nav-link");
  navLink.forEach((link, index) => {
    link.style.transitionDelay = isNavbarOpen ? `${index * 0.1}s` : "0s";
    link.style.opacity = isNavbarOpen ? "1" : "0";
    link.style.transform = isNavbarOpen ? "translateY(0)" : "translateY(-20px)";
  });

  // Muestra u oculta el elemento a.nav-link
  const hiddenNavLinks = document.querySelectorAll("a.nav-link.hidden");
  hiddenNavLinks.forEach(link => {
    link.classList.toggle("hidden");
  });
});