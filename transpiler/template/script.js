document.querySelector("#menu-link").addEventListener('click', (e) => {
    e.preventDefault()
    document.querySelector("#menu").style.display = 'flex';
})

document.querySelector("#goback").addEventListener('click', () => {
    document.querySelector("#menu").style.display = 'none';
})