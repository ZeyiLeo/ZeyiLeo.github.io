(() => {
  const button = document.querySelector(".navbar-toggler");
  const nav = document.querySelector("#navbarNav");

  if (!button || !nav) return;

  const setExpanded = (expanded) => {
    button.setAttribute("aria-expanded", String(expanded));
    button.classList.toggle("collapsed", !expanded);
    nav.classList.toggle("show", expanded);
  };

  button.addEventListener("click", () => {
    setExpanded(button.getAttribute("aria-expanded") !== "true");
  });

  nav.addEventListener("click", (event) => {
    if (event.target.closest("a")) setExpanded(false);
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") setExpanded(false);
  });

  const revealTargets = document.querySelectorAll(
    ".leo-section, .leo-closing, .leo-work-feature, .leo-work-strip a, .leo-contact-card, .leo-timeline article, .leo-project-hero, .leo-photo-grid figure"
  );

  if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches && "IntersectionObserver" in window) {
    revealTargets.forEach((target) => target.classList.add("leo-reveal"));

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.16 }
    );

    revealTargets.forEach((target) => observer.observe(target));
  }
})();
