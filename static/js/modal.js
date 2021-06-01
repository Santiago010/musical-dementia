const modal = document.querySelector(".modal");
const publications__actions = document.querySelector(
  ".publications__actions"
).firstElementChild;

publications__actions.onclick = () => {
  modal.style.visibility = "visible";
  document.body.children[1].style.opacity = "0.2";
};

modal.children[1].lastElementChild.onclick = () => {
  modal.style.visibility = "hidden";
  document.body.children[1].style.opacity = "1";
};
