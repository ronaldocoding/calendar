const password = document.querySelector(".password"),
    passwordEyeIcon = document.querySelector(".password-eye-icon"),
    confirmPassword = document.querySelector(".confirm-password"),
    confirmPasswordEyeIcon = document.querySelector(".confirm-password-eye-icon")

passwordEyeIcon.addEventListener("click", () => {
    if (password.type == "text") {
        password.type = "password"
        passwordEyeIcon.classList.replace("bx-hide", "bx-show")
    } else if (password.type == "password") {
        password.type = "text"
        passwordEyeIcon.classList.replace("bx-show", "bx-hide")
    }
})

confirmPasswordEyeIcon.addEventListener("click", () => {
    if (confirmPassword.type == "text") {
        confirmPassword.type = "password"
        confirmPasswordEyeIcon.classList.replace("bx-hide", "bx-show")
    } else if (confirmPassword.type == "password") {
        confirmPassword.type = "text"
        confirmPasswordEyeIcon.classList.replace("bx-show", "bx-hide")
    }
})