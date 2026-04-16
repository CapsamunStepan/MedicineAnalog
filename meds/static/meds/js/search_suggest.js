(() => {
  const forms = Array.from(document.querySelectorAll("form.search-form"));
  if (forms.length === 0) return;

  const debounce = (fn, ms) => {
    let t;
    return (...args) => {
      clearTimeout(t);
      t = setTimeout(() => fn(...args), ms);
    };
  };

  const escapeHtml = (str) =>
    String(str)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");

  const formatPrice = (v) => {
    if (v == null || v === "") return "";
    const n = Number(String(v).replace(",", "."));
    return Number.isFinite(n) ? n.toFixed(2) : String(v);
  };

  forms.forEach((form) => {
    const input = form.querySelector("input[name='query']");
    if (!input) return;

    let box = form.querySelector(".suggestions");
    if (!box) {
      box = document.createElement("div");
      box.className = "suggestions hidden";
      form.appendChild(box);
    }

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
          const isRecent = s.kind === "recent";
          const meta = [];
          if (isRecent) {
            meta.push('<span class="suggestion-icon">&#128339;</span>');
          }
          if (s.kind === "history" && s.count) meta.push(`${s.count}x`);
          if (s.min_price) meta.push(`de la ${formatPrice(s.min_price)} MDL`);
          const metaHtml = meta.length
            ? `<span class="suggestion-meta">${meta.join(" Â· ")}</span>`
            : "";
          return `
            <button type="button" class="suggestion${isRecent ? " suggestion--recent" : ""}"
                    data-text="${escapeHtml(s.text)}"
                    data-idx="${idx}">
              <span class="suggestion-text">${escapeHtml(s.text)}</span>
              ${metaHtml}
            </button>
          `;
        })
        .join("");
      open();
    };

    const fetchSuggestions = async () => {
      const q = input.value.trim();
      try {
        const res = await fetch(`/suggest/?q=${encodeURIComponent(q)}`, {
          headers: { Accept: "application/json" },
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

    input.addEventListener("focus", () => {
      if (input.value.trim().length < 2) fetchSuggestions();
    });

    box.addEventListener("click", (e) => {
      const btn = e.target.closest("button.suggestion");
      if (!btn) return;
      input.value = btn.dataset.text || "";
      close();
      form.submit();
    });

    document.addEventListener("click", (e) => {
      if (form.contains(e.target)) return;
      close();
    });

    input.addEventListener("keydown", (e) => {
      if (e.key === "Escape") close();
    });
  });
})();
