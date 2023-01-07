const forms = document.querySelector(".forms"),
    passwordHideShow = document.querySelectorAll(".eye-icon"),
    links = document.querySelectorAll(".link")

passwordHideShow.forEach(eyeIcon => {
    eyeIcon.addEventListener("click", () => {
        let passwordField = eyeIcon.parentElement.parentElement.querySelectorAll(".password")
        passwordField.forEach(password => {
            if (password.type == "password") {
                password.type = "text"
                eyeIcon.classList.replace("bx-show", "bx-hide")
            } else if (password.type == "text") {
                password.type = "password"
                eyeIcon.classList.replace("bx-hide", "bx-show")
            }
        })
    })
});