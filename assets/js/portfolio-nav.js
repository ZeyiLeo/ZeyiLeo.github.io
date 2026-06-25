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
})();
