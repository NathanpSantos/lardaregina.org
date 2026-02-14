document.addEventListener("DOMContentLoaded", () => {
  const modalHome = document.getElementById("modal-home");
  const buttonClose = document.getElementById("btn-close");

  if (!modalHome || !buttonClose) return;

  // abre só uma vez por sessão (opcional)
  
  if (!sessionStorage.getItem("modalHomeShown")) {
    modalHome.showModal();
    sessionStorage.setItem("modalHomeShown", "1");
  }

  buttonClose.addEventListener("click", () => modalHome.close());
});
