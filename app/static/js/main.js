(function () {
  const btn = document.getElementById("copyPixBtn");
  const msg = document.getElementById("copyPixMsg");
  if (!btn) return;

  btn.addEventListener("click", async () => {
    const pix = btn.getAttribute("data-pix") || "";
    try {
      await navigator.clipboard.writeText(pix);
      msg.textContent = "✅ Chave Pix copiada! Agora é só colar no seu app do banco.";
    } catch (e) {
      msg.textContent = "⚠️ Não consegui copiar automaticamente. Selecione e copie manualmente.";
    }
  });
})();


  const filterName = document.getElementById("filterName");
  const statusChecks = document.querySelectorAll(".filterStatus");
  const tipoChecks = document.querySelectorAll(".filterTipo");
  const clearBtn = document.getElementById("clearFilters");
  const cards = document.querySelectorAll(".adopt-card");

  function getCheckedValues(nodeList){
    return Array.from(nodeList).filter(i => i.checked).map(i => i.value);
  }

  function applyFilters(){
    const nameValue = (filterName.value || "").trim().toLowerCase();
    const statusValues = getCheckedValues(statusChecks);
    const tipoValues = getCheckedValues(tipoChecks);

    cards.forEach(card => {
      const nome = card.dataset.nome || "";
      const status = card.dataset.status || "";
      const tipo = card.dataset.tipo || "";

      const okName = !nameValue || nome.includes(nameValue);
      const okStatus = statusValues.length === 0 || statusValues.includes(status);
      const okTipo = tipoValues.length === 0 || tipoValues.includes(tipo);

      card.style.display = (okName && okStatus && okTipo) ? "" : "none";
    });
  }

  [filterName, ...statusChecks, ...tipoChecks].forEach(el => {
    el.addEventListener("input", applyFilters);
    el.addEventListener("change", applyFilters);
  });

  clearBtn?.addEventListener("click", () => {
    filterName.value = "";
    statusChecks.forEach(c => c.checked = false);
    tipoChecks.forEach(c => c.checked = false);
    applyFilters();
  });

  applyFilters();

  document.addEventListener("DOMContentLoaded", () => {
    const main = document.getElementById("mainPhoto");
    document.querySelectorAll(".thumb").forEach(btn => {
      btn.addEventListener("click", () => {
        main.src = btn.dataset.src;
      });
    });
  });
