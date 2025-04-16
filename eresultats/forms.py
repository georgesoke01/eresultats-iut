from django import forms
from .models import Reclamation


class MatriculeForm(forms.Form):
    matricule = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre matricule'})
    )

class ReclamationForm(forms.ModelForm):
    class Meta:
        model = Reclamation
        fields = ["sujet", "message"]
        widgets = {
            "sujet": forms.TextInput(attrs={"class": "form-control", "placeholder": "Sujet de la réclamation"}),
            "message": forms.Textarea(attrs={"class": "form-control", "placeholder": "Décrivez votre réclamation ici...", "rows": 4}),
        }
