document.addEventListener("DOMContentLoaded", () => {
  const modal = document.getElementById("campanhaModal");
  if (!modal) return;

  // Só na HOME
  const isHome = window.__IS_HOME__ === true;
  if (!isHome) return;

  // abre 2s depois
  setTimeout(() => {
    if (!modal.open) modal.showModal();
  }, 2000);

  const closeBtn = document.getElementById("campanhaClose");
  const laterBtn = document.getElementById("campanhaLater");

  function closeModal(){ modal.close(); }

  closeBtn?.addEventListener("click", (e) => { e.preventDefault(); closeModal(); });
  laterBtn?.addEventListener("click", closeModal);

  modal.addEventListener("click", (e) => {
    const box = modal.querySelector(".campanha-box");
    if (box && !box.contains(e.target)) closeModal();
  });
});
