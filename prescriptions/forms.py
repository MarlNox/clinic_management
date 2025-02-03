# prescriptions/forms.py
from django import forms
from .models import Prescription

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['patient', 'medications', 'notes']
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'medications': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
