from django.shortcuts import render, get_object_or_404
from .models import ExamConcours

def index(request):
    examens_concours = ExamConcours.objects.all().order_by('numero_ordre')
    return render(request, 'index.html', {'examens_concours': examens_concours})

def all_result(request):
    examens_concours = ExamConcours.objects.order_by('-date_creation')[:6]
    return render(request, 'all_result.html', {'examens_concours': examens_concours})

"""def resultat_examen(request, slug):
    examen = get_object_or_404(ExamConcours, slug=slug)
    return render(request, 'resultat_examen.html', {'examen': examen})

"""