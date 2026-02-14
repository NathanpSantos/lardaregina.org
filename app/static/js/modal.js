document.addEventListener("DOMContentLoaded", () => {
  const modal = document.getElementById("campanhaModal");
  const closeBtn = document.getElementById("campanhaClose");
  const laterBtn = document.getElementById("campanhaLater");

  if (!modal) return;

  // 🔥 abre SEMPRE que a página carregar
  if (window.location.pathname === "/") {
    modal.showModal();
  }



  function closeModal() {
    modal.close();
  }

  closeBtn?.addEventListener("click", (e) => {
    e.stopPropagation();
    closeModal();
  });

  laterBtn?.addEventListener("click", () => {
    closeModal();
  });

  // clicar fora fecha
  modal.addEventListener("click", (e) => {
    const box = modal.querySelector(".campanha-box");
    if (!box) return;
    const clickedOutside = !box.contains(e.target);
    if (clickedOutside) closeModal();
  });
});
