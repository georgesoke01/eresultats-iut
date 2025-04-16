from django.db import models

class Etudiant(models.Model):
    SEXE_CHOICES =[
        ("M", "Masculin"),
        ("F", "Féminin"),
        ]
    
    NIVEAU_CHOICES = [
        ("Licence professionnelle 1", "L1"),
        ("Licence professionnelle 2", "L2"),
        ("Licence professionnelle 3", "L3"),
        ("Master professionnelle 1", "M1"),
        ("Master professionnelle 2", "M2"),
    ]
    
    matricule = models.CharField(max_length= 20, unique=True)
    nom = models.CharField(max_length=100)
    prenoms = models.CharField(max_length=200)
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES)
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=100)
    niveau_etude = models.CharField(max_length=30, choices=NIVEAU_CHOICES)
    
    def __str__(self):
        return f"{self.matricule} - {self.nom} {self.prenoms}"
    

class Note(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    matiere = models.CharField(max_length=100)
    note = models.FloatField()
    semestre = models.IntegerField()
    
    def __str__(self):
        return f"{self.etudiant} - {self.matiere}: {self.note}"
    

class ConfigSite(models.Model):
    reclamations_actives = models.BooleanField(default=True)

    def __str__(self):
        return "Configuration du site"

class Reclamation(models.Model):
    etudiant = models.ForeignKey("Etudiant", on_delete=models.CASCADE)
    sujet = models.CharField(max_length=255)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(
        max_length=20,
        choices=[("En attente", "En attente"), ("Traitée", "Traitée"), ("Rejetée", "Rejetée")],
        default="En attente",
    )

    def __str__(self):
        return f"Réclamation de {self.etudiant.matricule} - {self.sujet}"

    