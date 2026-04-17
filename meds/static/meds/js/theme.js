(() => {
  const STORAGE_KEY = "ma-theme";
  const CYCLE = ["light", "dark", "system"];
  const ICONS = { light: "\u2600\uFE0F", dark: "\uD83C\uDF19", system: "\uD83D\uDCBB" };

  function getPreferred() {
    return localStorage.getItem(STORAGE_KEY) || "system";
  }

  function resolveTheme(mode) {
    if (mode === "system") {
      return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
    }
    return mode;
  }

  function getTitles(button) {
    return {
      light: button.dataset.titleLight || "Light theme",
      dark: button.dataset.titleDark || "Dark theme",
      system: button.dataset.titleSystem || "Use system theme",
    };
  }

  function apply(mode) {
    document.documentElement.setAttribute("data-theme", resolveTheme(mode));
    document.querySelectorAll(".theme-toggle").forEach((button) => {
      const titles = getTitles(button);
      button.innerHTML = ICONS[mode];
      button.title = titles[mode];
      button.setAttribute("aria-label", titles[mode]);
      button.dataset.mode = mode;
    });
  }

  apply(getPreferred());

  window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", () => {
    if (getPreferred() === "system") apply("system");
  });

  document.addEventListener("click", (event) => {
    const button = event.target.closest(".theme-toggle");
    if (!button) return;
    const current = getPreferred();
    const next = CYCLE[(CYCLE.indexOf(current) + 1) % CYCLE.length];
    localStorage.setItem(STORAGE_KEY, next);
    apply(next);
  });
})();
