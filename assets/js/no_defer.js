document.addEventListener("DOMContentLoaded", () => {
  const isDark = document.documentElement.getAttribute("data-theme") === "dark";

  document.querySelectorAll("table").forEach((table) => {
    table.classList.toggle("table-dark", isDark);

    const excluded = table.closest('[class*="news"], [class*="card"], code');
    if (!excluded) {
      table.classList.add("table-hover");
    }
  });
});
