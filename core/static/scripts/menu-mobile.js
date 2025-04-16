document.addEventListener("DOMContentLoaded", ()=>{
    const menuIcon = document.getElementById("menu-icon");
    const menu = document.getElementById("menu-list");

    menuIcon.addEventListener("click", ()=>{
        menu.classList.toggle("active");
        menuIcon.classList.toggle("active");
    });
});