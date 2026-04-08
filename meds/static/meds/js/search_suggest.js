(() => {
  const form = document.querySelector("form.search-form");
  if (!form) return;

  const input = form.querySelector("input[name='query']");
  const modeSelect = form.querySelector("select[name='mode']");
  if (!input || !modeSelect) return;

  let box = document.getElementById("suggestions");
  if (!box) {
    box = document.createElement("div");
    box.id = "suggestions";
    box.className = "suggestions hidden";
    form.appendChild(box);
  }

  const debounce = (fn, ms) => {
    let t;
    return (...args) => {
      clearTimeout(t);
      t = setTimeout(() => fn(...args), ms);
    };
  };

  const close = () => {
    box.classList.add("hidden");
    box.innerHTML = "";
  };

  const open = () => {
    box.classList.remove("hidden");
  };

  const render = (items) => {
    if (!items || items.length === 0) {
      close();
      return;
    }

    box.innerHTML = items
      .map((s, idx) => {
        const meta = [];
        if (s.kind === "history" && s.count) meta.push(`${s.count}x`);
        if (s.min_price) meta.push(`de la ${s.min_price} MDL`);
        const metaText = meta.length ? `<span class="suggestion-meta">${meta.join(" · ")}</span>` : "";
        return `
          <button type="button" class="suggestion" data-text="${escapeHtml(s.text)}" data-idx="${idx}">
            <span class="suggestion-text">${escapeHtml(s.text)}</span>
            ${metaText}
          </button>
        `;
      })
      .join("");
    open();
  };

  const escapeHtml = (str) =>
    String(str)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");

  const fetchSuggestions = async () => {
    const q = input.value.trim();
    const mode = modeSelect.value;
    if (q.length < 2) {
      close();
      return;
    }
    try {
      const res = await fetch(`/suggest/?q=${encodeURIComponent(q)}&mode=${encodeURIComponent(mode)}`, {
        headers: { "Accept": "application/json" },
      });
      if (!res.ok) {
        close();
        return;
      }
      const data = await res.json();
      render(data.suggestions || []);
    } catch {
      close();
    }
  };

  const debouncedFetch = debounce(fetchSuggestions, 160);

  input.addEventListener("input", debouncedFetch);
  modeSelect.addEventListener("change", debouncedFetch);

  box.addEventListener("click", (e) => {
    const btn = e.target.closest("button.suggestion");
    if (!btn) return;
    input.value = btn.dataset.text || "";
    close();
    form.submit();
  });

  document.addEventListener("click", (e) => {
    if (e.target === input || box.contains(e.target)) return;
    close();
  });

  input.addEventListener("keydown", (e) => {
    if (e.key === "Escape") close();
  });
})();

