const hideAlert = () => {
  let containerToHide = document.querySelector('.form-alert-container')
  containerToHide.style.display = "none";
}

const addAlertDismissListener = () => {
    let dismissButton = document.querySelector('.form-alert-dismiss-button')
    dismissButton.addEventListener('click', hideAlert)
}

addAlertDismissListener()