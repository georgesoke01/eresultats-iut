document.addEventListener("DOMContentLoaded", function () {
    const params = new URLSearchParams(window.location.search);
    const examName = params.get("exam");
    const matriculeInput = document.getElementById("matricule");
    const menuToggle = document.querySelector(".menu-toggle");
    const navMenu = this.getElementById("navMenu");

    menuToggle.addEventListener("click", ()=>{
        navMenu.classList.toggle("show");
    });

    // Afficher le nom de l'examen sur la page matricule.html
    if (document.getElementById("exam-title") && examName) {
        document.getElementById("exam-title").innerText = `Vérification du matricule - ${examName}`;
    }

    // Gestion du formulaire de matricule
    const form = document.getElementById("matriculeForm");
    if (form) {
        form.addEventListener("submit", function (e) {
            e.preventDefault();
            const matricule = matriculeInput.value;
            window.location.href = `resultat.html?exam=${examName}&matricule=${matricule}`;
        });
    }

    // Affichage du résultat sur resultat.html
    const matriculeResult = document.getElementById("matricule-result");
    if (matriculeResult) {
        const matricule = params.get("matricule");
        document.getElementById("exam-name").innerText = `Examen : ${examName}`;
        matriculeResult.innerText = `Matricule : ${matricule}`;
    }
});
