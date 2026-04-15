(() => {
  const STORAGE_KEY = "ma-theme";
  const CYCLE = ["light", "dark", "system"];
  const ICONS = { light: "\u2600\uFE0F", dark: "\uD83C\uDF19", system: "\uD83D\uDCBB" };
  const TITLES = { light: "Светлая тема", dark: "Тёмная тема", system: "Как в системе" };

  function getPreferred() {
    return localStorage.getItem(STORAGE_KEY) || "system";
  }

  function resolveTheme(mode) {
    if (mode === "system") {
      return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
    }
    return mode;
  }

  function apply(mode) {
    document.documentElement.setAttribute("data-theme", resolveTheme(mode));
    document.querySelectorAll(".theme-toggle").forEach((btn) => {
      btn.innerHTML = ICONS[mode];
      btn.title = TITLES[mode];
      btn.dataset.mode = mode;
    });
  }

  apply(getPreferred());

  window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", () => {
    if (getPreferred() === "system") apply("system");
  });

  document.addEventListener("click", (e) => {
    const btn = e.target.closest(".theme-toggle");
    if (!btn) return;
    const current = getPreferred();
    const next = CYCLE[(CYCLE.indexOf(current) + 1) % CYCLE.length];
    localStorage.setItem(STORAGE_KEY, next);
    apply(next);
  });
})();
