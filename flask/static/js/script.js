document.querySelector("#menu-link").addEventListener('click', (e) => {
    e.preventDefault()
    document.querySelector("#menu").style.display = 'flex';
})

document.querySelector("#goback").addEventListener('click', () => {
    document.querySelector("#menu").style.display = 'none';
})

document.querySelector("#custom-file-btn").addEventListener("click", (e) => {
    e.preventDefault()
    document.querySelector("#file-input").click()
    console.log("Clicked")
})


document.querySelector("#file-input").addEventListener("change", () => {
    document.querySelector("#form").submit()
})