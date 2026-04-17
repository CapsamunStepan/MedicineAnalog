(() => {
  const dialogs = Array.from(document.querySelectorAll(".language-dialog"));
  if (dialogs.length === 0) return;

  const GAP = 8;
  const VIEWPORT_PADDING = 12;

  const setExpanded = (dialog, expanded) => {
    document.querySelectorAll(`[data-dialog-id="${dialog.id}"]`).forEach((button) => {
      button.setAttribute("aria-expanded", expanded ? "true" : "false");
    });
  };

  const closeDialog = (dialog) => {
    if (!dialog.open) return;
    dialog.close();
    setExpanded(dialog, false);
    dialog._trigger = null;
  };

  const positionDialog = (dialog) => {
    const trigger = dialog._trigger;
    if (!trigger) return;

    const rect = trigger.getBoundingClientRect();
    const dialogWidth = dialog.offsetWidth;
    const dialogHeight = dialog.offsetHeight;

    let left = rect.right - dialogWidth;
    left = Math.max(VIEWPORT_PADDING, Math.min(left, window.innerWidth - dialogWidth - VIEWPORT_PADDING));

    let top = rect.bottom + GAP;
    if (top + dialogHeight > window.innerHeight - VIEWPORT_PADDING) {
      top = Math.max(VIEWPORT_PADDING, rect.top - dialogHeight - GAP);
    }

    dialog.style.left = `${left}px`;
    dialog.style.top = `${top}px`;
  };

  const openDialog = (dialog, trigger) => {
    dialogs.forEach((candidate) => {
      if (candidate !== dialog) closeDialog(candidate);
    });

    dialog._trigger = trigger;
    if (!dialog.open) {
      dialog.show();
    }
    setExpanded(dialog, true);
    positionDialog(dialog);
  };

  dialogs.forEach((dialog) => {
    dialog.addEventListener("close", () => {
      setExpanded(dialog, false);
      dialog._trigger = null;
    });
  });

  const repositionOpenDialogs = () => {
    dialogs.forEach((dialog) => {
      if (dialog.open) positionDialog(dialog);
    });
  };

  window.addEventListener("resize", repositionOpenDialogs);
  window.addEventListener("scroll", repositionOpenDialogs, true);

  document.addEventListener("click", (event) => {
    const trigger = event.target.closest("[data-language-trigger]");
    if (trigger) {
      const dialog = document.getElementById(trigger.dataset.dialogId);
      if (!dialog) return;

      if (dialog.open) {
        closeDialog(dialog);
      } else {
        openDialog(dialog, trigger);
      }
      return;
    }

    const clickedInsideDialog = event.target.closest(".language-dialog");
    if (!clickedInsideDialog) {
      dialogs.forEach(closeDialog);
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      dialogs.forEach(closeDialog);
    }
  });
})();
