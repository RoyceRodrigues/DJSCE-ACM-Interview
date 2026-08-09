function toggleMenu() {
  let menu = document.getElementById("menu");

  menu.classList.toggle("active");
}

// Close menu after clicking link

let links = document.querySelectorAll("nav a");

links.forEach((link) => {
  link.onclick = function () {
    document.getElementById("menu").classList.remove("active");
  };
});

// Scroll animation

window.addEventListener("scroll", () => {
  let sections = document.querySelectorAll("section");

  sections.forEach((section) => {
    let position = section.getBoundingClientRect().top;

    if (position < window.innerHeight - 100) {
      section.style.opacity = "1";
      section.style.transform = "translateY(0)";
    }
  });
});

// Initial animation

document.querySelectorAll("section").forEach((section) => {
  section.style.opacity = "0";
  section.style.transform = "translateY(50px)";
  section.style.transition = "0.8s";
});
