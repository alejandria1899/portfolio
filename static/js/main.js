document.addEventListener("DOMContentLoaded", () => {
  const navToggle = document.querySelector(".nav-toggle");
  const navMenu = document.querySelector(".nav-menu");

  // Menú móvil
  if (navToggle && navMenu) {
    const toggle = () => {
      navMenu.classList.toggle("active");
      navToggle.classList.toggle("active");
    };

    navToggle.addEventListener("click", toggle);

    // accesibilidad (enter/space)
    navToggle.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " ") toggle();
    });

    // cerrar menú al clicar link
    navMenu.querySelectorAll("a").forEach((a) => {
      a.addEventListener("click", () => {
        navMenu.classList.remove("active");
        navToggle.classList.remove("active");
      });
    });
  }

  // Smooth scroll con offset (navbar)
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", (e) => {
      const href = anchor.getAttribute("href");
      const target = document.querySelector(href);
      if (!target) return;

      e.preventDefault();
      const yOffset = 78;
      const y = target.getBoundingClientRect().top + window.scrollY - yOffset;
      window.scrollTo({ top: y, behavior: "smooth" });
    });
  });

  // Animación barras habilidades (suave)
  const about = document.querySelector("#sobre-mi");
  if (about) {
    const bars = about.querySelectorAll(".skill-progress");
    bars.forEach((bar) => {
      const finalWidth = bar.style.width;
      bar.dataset.finalWidth = finalWidth;
      bar.style.width = "0%";
    });

    const obs = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          bars.forEach((bar, idx) => {
            setTimeout(() => {
              bar.style.width = bar.dataset.finalWidth || "0%";
            }, idx * 80);
          });
          obs.disconnect();
        });
      },
      { threshold: 0.25 }
    );

    obs.observe(about);
  }

  // Formulario (demo)
  const contactForm = document.getElementById("contactForm");
  if (contactForm) {
    contactForm.addEventListener("submit", (e) => {
      e.preventDefault();

      const btn = contactForm.querySelector('button[type="submit"]');
      if (btn) {
        const oldText = btn.textContent;
        btn.textContent = "Enviado";
        btn.disabled = true;

        setTimeout(() => {
          btn.textContent = oldText || "Enviar Mensaje";
          btn.disabled = false;
          contactForm.reset();
        }, 1300);
      } else {
        contactForm.reset();
      }
    });
  }
});
