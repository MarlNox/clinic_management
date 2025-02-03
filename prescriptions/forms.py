# prescriptions/forms.py
from django import forms
from .models import Prescription, Medication

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['patient', 'medications', 'notes']
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'medications': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

# NEW: Medication form for adding new medications
class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = ['name', 'dosage_instructions']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dosage_instructions': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
