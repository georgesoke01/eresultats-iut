from django.shortcuts import render, redirect, get_object_or_404
from .models import Etudiant, Note, ConfigSite
from .forms import MatriculeForm, ReclamationForm
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from core.models import ExamConcours

def recherche_resultats(request, slug):
    form = MatriculeForm()
    etudiant = None
    notes = None
    notes_non_validees = None
    message = ""
    reclamations_actives = ConfigSite.objects.first().reclamations_actives if ConfigSite.objects.exists() else True
    examen = get_object_or_404(ExamConcours, slug=slug)


    if request.method == "POST":
        form = MatriculeForm(request.POST)
        if form.is_valid():
            matricule = form.cleaned_data['matricule']
            try:
                etudiant = Etudiant.objects.get(matricule=matricule)
                notes = Note.objects.filter(etudiant=etudiant)
                notes_non_validees = notes.filter(note__lt=12)  # Filtrer les matières non validées
            except Etudiant.DoesNotExist:
                message = "Aucun étudiant trouvé avec ce matricule."

    # Statistiques
    ue_validees = notes.filter(note__gte=12).count() if notes else 0
    ue_non_validees = notes.filter(note__lt=12).count() if notes else 0

    return render(request, "recherche_resultats.html", {
        "examen": examen,
        "form": form,
        "etudiant": etudiant,
        "notes": notes,
        "notes_non_validees": notes_non_validees,
        "message": message,
        "reclamations_actives": reclamations_actives,
        "ue_validees": ue_validees,
        "ue_non_validees": ue_non_validees,
    })



def export_pdf(request, matricule):
    try:
        etudiant = Etudiant.objects.get(matricule=matricule)
        notes = Note.objects.filter(etudiant=etudiant)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{matricule}_resultats.pdf"'

        p = canvas.Canvas(response)
        p.drawString(100, 800, f"Résultats de {etudiant.nom} {etudiant.prenoms} ({matricule})")

        y = 780
        for note in notes:
            y -= 20
            p.drawString(100, y, f"{note.matiere}: {note.note}")

        p.showPage()
        p.save()
        return response
    except Etudiant.DoesNotExist:
        return HttpResponse("Matricule introuvable", status=404)
    
def deposer_reclamation(request, matricule):
    try:
        etudiant = Etudiant.objects.get(matricule=matricule)
    except Etudiant.DoesNotExist:
        return render(request, "reclamation.html", {"message": "Aucun étudiant trouvé avec ce matricule."})

    if request.method == "POST":
        form = ReclamationForm(request.POST)
        if form.is_valid():
            reclamation = form.save(commit=False)
            reclamation.etudiant = etudiant
            reclamation.save()
            return redirect("confirmation_reclamation")  # Redirection après soumission

    else:
        form = ReclamationForm()

    return render(request, "reclamation.html", {"form": form, "etudiant": etudiant})

def confirmation_reclamation(request):
    return render(request, "confirmation_reclamation.html")

