const password = document.querySelector(".password"),
    passwordEyeIcon = document.querySelector(".eye-icon")

passwordEyeIcon.addEventListener("click", () => {
    if (password.type == "password") {
        password.type = "text"
        passwordEyeIcon.classList.replace("bx-show", "bx-hide")
    } else if (password.type == "text") {
        password.type = "password"
        passwordEyeIcon.classList.replace("bx-hide", "bx-show")
    }
})