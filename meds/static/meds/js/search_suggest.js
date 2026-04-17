(() => {
  const forms = Array.from(document.querySelectorAll("form.search-form"));
  if (forms.length === 0) return;

  const DEBOUNCE_MS = 450;
  const MIN_QUERY_LENGTH = 2;
  const HISTORY_DELETE_URL = "/search-history/delete/";
  const HISTORY_CLEAR_URL = "/search-history/clear/";
  const REMOVE_ICON = `
    <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false">
      <path d="M4 4l8 8m0-8l-8 8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
    </svg>
  `;

  const debounce = (fn, ms) => {
    let timerId;
    return (...args) => {
      clearTimeout(timerId);
      timerId = setTimeout(() => fn(...args), ms);
    };
  };

  const escapeHtml = (str) =>
    String(str)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");

  const formatPrice = (value) => {
    if (value == null || value === "") return "";
    const normalized = Number(String(value).replace(",", "."));
    return Number.isFinite(normalized) ? normalized.toFixed(2) : String(value);
  };

  const getCookie = (name) => {
    const prefix = `${name}=`;
    const cookie = document.cookie
      .split(";")
      .map((part) => part.trim())
      .find((part) => part.startsWith(prefix));

    return cookie ? decodeURIComponent(cookie.slice(prefix.length)) : "";
  };

  const postHistoryAction = async (url, payload = {}) => {
    const headers = {
      Accept: "application/json",
      "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    };
    const csrfToken = getCookie("csrftoken");
    if (csrfToken) {
      headers["X-CSRFToken"] = csrfToken;
    }

    const response = await fetch(url, {
      method: "POST",
      headers,
      body: new URLSearchParams(payload).toString(),
    });

    if (!response.ok) {
      throw new Error(`History request failed with status ${response.status}`);
    }

    return response.json();
  };

  forms.forEach((form) => {
    const input = form.querySelector("input[name='query']");
    if (!input) return;

    const clearButton = form.querySelector(".search-clear");
    const historyTitle = form.dataset.historyTitle || "Recent history";
    const clearHistoryLabel = form.dataset.clearHistory || "Clear all";
    const removeHistoryLabel = form.dataset.removeHistory || "Remove from history";
    const fromLabel = form.dataset.fromLabel || "from";

    let activeRequestController = null;
    let requestToken = 0;
    let isHistoryActionPending = false;

    let box = form.querySelector(".suggestions");
    if (!box) {
      box = document.createElement("div");
      box.className = "suggestions hidden";
      form.appendChild(box);
    }

    const updateClearButton = () => {
      if (!clearButton) return;
      clearButton.hidden = input.value.trim().length === 0;
    };

    const close = () => {
      box.classList.add("hidden");
      box.innerHTML = "";
    };

    const open = () => {
      box.classList.remove("hidden");
    };

    const abortActiveRequest = () => {
      if (!activeRequestController) return;
      activeRequestController.abort();
      activeRequestController = null;
    };

    const render = (items) => {
      if (!items || items.length === 0) {
        close();
        return;
      }

      const allAreRecent = items.every((item) => item.kind === "recent");
      const headerHtml = allAreRecent
        ? `
            <div class="suggestions-header">
              <span class="suggestions-title">${escapeHtml(historyTitle)}</span>
              <button type="button" class="suggestions-clear-all" data-action="clear-history">
                ${escapeHtml(clearHistoryLabel)}
              </button>
            </div>
          `
        : "";

      const itemsHtml = items
        .map((item, index) => {
          const meta = [];
          if (item.count) meta.push(`${item.count}x`);
          if (item.min_price) meta.push(`${fromLabel} ${formatPrice(item.min_price)} MDL`);
          const metaHtml = meta.length
            ? `<span class="suggestion-meta">${meta.join(" &middot; ")}</span>`
            : "";

          if (item.kind === "recent") {
            return `
              <div class="suggestion-row suggestion-row--recent">
                <button type="button" class="suggestion suggestion--recent"
                        data-text="${escapeHtml(item.text)}"
                        data-idx="${index}">
                  <span class="suggestion-copy">
                    <span class="suggestion-text">${escapeHtml(item.text)}</span>
                  </span>
                </button>
                <button type="button"
                        class="suggestion-remove"
                        data-action="remove-history"
                        data-text="${escapeHtml(item.text)}"
                        aria-label="${escapeHtml(removeHistoryLabel)}"
                        title="${escapeHtml(removeHistoryLabel)}">
                  ${REMOVE_ICON}
                </button>
              </div>
            `;
          }

          return `
            <button type="button" class="suggestion"
                    data-text="${escapeHtml(item.text)}"
                    data-idx="${index}">
              <span class="suggestion-copy">
                <span class="suggestion-text">${escapeHtml(item.text)}</span>
                ${metaHtml}
              </span>
            </button>
          `;
        })
        .join("");

      box.innerHTML = `${headerHtml}${itemsHtml}`;
      open();
    };

    const requestSuggestions = async (query) => {
      const requestedQuery = query ?? input.value.trim();
      if (requestedQuery !== "" && requestedQuery.length < MIN_QUERY_LENGTH) {
        abortActiveRequest();
        close();
        return;
      }

      abortActiveRequest();
      const controller = new AbortController();
      const currentToken = ++requestToken;
      activeRequestController = controller;

      try {
        const response = await fetch(`/suggest/?q=${encodeURIComponent(requestedQuery)}`, {
          headers: { Accept: "application/json" },
          signal: controller.signal,
        });
        if (!response.ok) {
          close();
          return;
        }

        const data = await response.json();
        if (currentToken !== requestToken || input.value.trim() !== requestedQuery) {
          return;
        }

        render(data.suggestions || []);
      } catch (error) {
        if (error.name === "AbortError") {
          return;
        }
        close();
      } finally {
        if (activeRequestController === controller) {
          activeRequestController = null;
        }
      }
    };

    const debouncedFetch = debounce(() => requestSuggestions(), DEBOUNCE_MS);

    input.addEventListener("input", () => {
      updateClearButton();
      if (input.value.trim().length < MIN_QUERY_LENGTH) {
        abortActiveRequest();
        close();
        return;
      }

      debouncedFetch();
    });

    input.addEventListener("focus", () => {
      updateClearButton();
      if (input.value.trim().length < MIN_QUERY_LENGTH) {
        requestSuggestions("");
      }
    });

    if (clearButton) {
      clearButton.addEventListener("click", () => {
        input.value = "";
        updateClearButton();
        abortActiveRequest();
        close();
        input.focus();
      });
    }

    box.addEventListener("click", async (event) => {
      const clearHistoryButton = event.target.closest("button[data-action='clear-history']");
      if (clearHistoryButton) {
        event.preventDefault();
        if (isHistoryActionPending) return;

        isHistoryActionPending = true;
        try {
          const data = await postHistoryAction(HISTORY_CLEAR_URL);
          render(data.suggestions || []);
          input.focus();
        } catch {
          close();
        } finally {
          isHistoryActionPending = false;
        }
        return;
      }

      const removeHistoryButton = event.target.closest("button[data-action='remove-history']");
      if (removeHistoryButton) {
        event.preventDefault();
        event.stopPropagation();
        if (isHistoryActionPending) return;

        isHistoryActionPending = true;
        try {
          const data = await postHistoryAction(HISTORY_DELETE_URL, {
            query: removeHistoryButton.dataset.text || "",
          });
          render(data.suggestions || []);
          input.focus();
        } catch {
          close();
        } finally {
          isHistoryActionPending = false;
        }
        return;
      }

      const suggestionButton = event.target.closest("button.suggestion");
      if (!suggestionButton) return;

      input.value = suggestionButton.dataset.text || "";
      updateClearButton();
      close();
      form.submit();
    });

    document.addEventListener("click", (event) => {
      if (form.contains(event.target)) return;
      abortActiveRequest();
      close();
    });

    input.addEventListener("keydown", (event) => {
      if (event.key === "Escape") {
        abortActiveRequest();
        close();
      }
    });

    updateClearButton();
  });
})();
