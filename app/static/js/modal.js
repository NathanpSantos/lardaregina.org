document.addEventListener("DOMContentLoaded", () => {
  const modal = document.getElementById("campanhaModal");
  const closeBtn = document.getElementById("campanhaClose");
  const laterBtn = document.getElementById("campanhaLater");

  if (!modal) return;

  // abre 2s depois (premium: não assusta)
  setTimeout(() => {
    modal.showModal();
  }, 2000);

  function closeModal(){
    modal.close();
  }

  closeBtn?.addEventListener("click", (e) => {
    e.preventDefault();
    e.stopPropagation();
    closeModal();
  });

  laterBtn?.addEventListener("click", () => closeModal());

  // clicar fora fecha
  modal.addEventListener("click", (e) => {
    const box = modal.querySelector(".campanha-box");
    if (!box) return;
    if (!box.contains(e.target)) closeModal();
  });

  // ESC já fecha automaticamente pelo dialog
});
