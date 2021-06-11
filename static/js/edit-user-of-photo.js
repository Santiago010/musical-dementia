const containerEditPhotoInput = document.querySelector(
  ".container-edit-photo__input"
);

const containerEditPhotoButton = document.querySelector(
  ".container-edit-photo__button"
);
const containerEditPhotoSpan = document.querySelector(
  ".container-edit-photo__span"
);

containerEditPhotoButton.addEventListener("click", () => {
  containerEditPhotoInput.click();
});

containerEditPhotoInput.addEventListener("change", () => {
  if (containerEditPhotoInput.value) {
    containerEditPhotoSpan.innerHTML = containerEditPhotoInput.value.match(
      /[\/\\]([\w\d\s\.\-\(\)]+)$/
    )[1];
  } else {
    containerEditPhotoSpan.innerHTML = "Escoge un foto para tu perfil";
  }
});
