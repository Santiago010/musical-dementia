const modal = document.querySelector(".modal");
const publications__actions = document.querySelector(".actions__delete");

publications__actions.onclick = () => {
  modal.style.visibility = "visible";
  document.body.children[1].style.opacity = "0.2";
};

modal.children[1].lastElementChild.onclick = () => {
  modal.style.visibility = "hidden";
  document.body.children[1].style.opacity = "1";
};
