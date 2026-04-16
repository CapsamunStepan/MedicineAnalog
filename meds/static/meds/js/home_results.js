(() => {
  const tabs = Array.from(document.querySelectorAll(".pharmacy-tab"));
  const panels = Array.from(document.querySelectorAll(".pharmacy-panel"));
  if (tabs.length === 0 || panels.length === 0) return;

  const getPaginationRange = (currentPage, totalPages) => {
    if (totalPages <= 7) {
      return Array.from({ length: totalPages }, (_, idx) => idx + 1);
    }

    const pages = [1];
    const start = Math.max(2, currentPage - 1);
    const end = Math.min(totalPages - 1, currentPage + 1);

    if (start > 2) pages.push("ellipsis-left");
    for (let page = start; page <= end; page += 1) pages.push(page);
    if (end < totalPages - 1) pages.push("ellipsis-right");

    pages.push(totalPages);
    return pages;
  };

  const panelState = new WeakMap();

  const renderPagination = (panel, requestedPage) => {
    const state = panelState.get(panel);
    if (!state) return;

    const { cards, pagination, pageSize } = state;
    const totalPages = Math.max(1, Math.ceil(cards.length / pageSize));
    const currentPage = Math.min(Math.max(requestedPage ?? state.currentPage, 1), totalPages);
    state.currentPage = currentPage;

    const start = (currentPage - 1) * pageSize;
    const end = start + pageSize;

    cards.forEach((card, idx) => {
      card.hidden = idx < start || idx >= end;
    });

    if (totalPages <= 1) {
      pagination.hidden = true;
      pagination.innerHTML = "";
      return;
    }

    const pageButtons = getPaginationRange(currentPage, totalPages)
      .map((item) => {
        if (typeof item !== "number") {
          return '<span class="results-pagination__ellipsis" aria-hidden="true">...</span>';
        }

        const activeClass = item === currentPage ? " is-active" : "";
        const ariaCurrent = item === currentPage ? ' aria-current="page"' : "";
        return `
          <button type="button" class="results-pagination__btn${activeClass}" data-page="${item}"${ariaCurrent}>
            ${item}
          </button>
        `;
      })
      .join("");

    pagination.innerHTML = `
      <button type="button" class="results-pagination__btn results-pagination__btn--nav" data-page="${currentPage - 1}" ${currentPage === 1 ? "disabled" : ""}>
        Inapoi
      </button>
      <div class="results-pagination__pages" aria-label="Paginare rezultate">
        ${pageButtons}
      </div>
      <button type="button" class="results-pagination__btn results-pagination__btn--nav" data-page="${currentPage + 1}" ${currentPage === totalPages ? "disabled" : ""}>
        Inainte
      </button>
    `;
    pagination.hidden = false;
  };

  panels.forEach((panel) => {
    const cards = Array.from(panel.querySelectorAll(".medicine-card"));
    const pagination = panel.querySelector(".results-pagination");
    if (!pagination) return;

    panelState.set(panel, {
      cards,
      pagination,
      pageSize: Number(pagination.dataset.pageSize || 10),
      currentPage: 1,
    });

    pagination.addEventListener("click", (event) => {
      const button = event.target.closest("button[data-page]");
      if (!button || button.disabled) return;

      const nextPage = Number(button.dataset.page);
      if (!Number.isFinite(nextPage)) return;
      renderPagination(panel, nextPage);
    });

    renderPagination(panel, 1);
  });

  const activatePanel = (pharmacyId) => {
    tabs.forEach((tab) => {
      tab.classList.toggle("active", tab.dataset.pharmacy === pharmacyId);
    });

    panels.forEach((panel) => {
      const isActive = panel.dataset.pharmacy === pharmacyId;
      panel.classList.toggle("active", isActive);
      if (isActive) {
        const state = panelState.get(panel);
        renderPagination(panel, state?.currentPage ?? 1);
      }
    });
  };

  tabs.forEach((tab) => {
    tab.addEventListener("click", () => {
      activatePanel(tab.dataset.pharmacy);
    });
  });
})();
