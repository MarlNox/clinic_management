# prescriptions/forms.py

from django import forms
from django.forms import inlineformset_factory
from .models import Prescription, Medication, PrescriptionMedication, ActivePrinciple

# --- Form for Prescription (unchanged) ---
class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['patient', 'notes']
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

# --- Form for PrescriptionMedication (unchanged) ---
class PrescriptionMedicationForm(forms.ModelForm):
    class Meta:
        model = PrescriptionMedication
        fields = ['medication', 'dosage', 'frequency']
        widgets = {
            'medication': forms.Select(attrs={'class': 'form-control'}),
            'dosage': forms.TextInput(attrs={'class': 'form-control'}),
            'frequency': forms.TextInput(attrs={'class': 'form-control'}),
        }

PrescriptionMedicationFormSet = inlineformset_factory(
    Prescription,
    PrescriptionMedication,
    form=PrescriptionMedicationForm,
    extra=1,
    can_delete=True
)

# --- Updated Medication form with new fields ---
class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = ['brand_name', 'generic_name', 'dosage_form', 'drug_class', 'dosage_instructions']
        widgets = {
            'brand_name': forms.TextInput(attrs={'class': 'form-control'}),
            'generic_name': forms.TextInput(attrs={'class': 'form-control'}),
            'dosage_form': forms.TextInput(attrs={'class': 'form-control'}),
            'drug_class': forms.TextInput(attrs={'class': 'form-control'}),
            'dosage_instructions': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

# --- Form for an Active Principle ---
class ActivePrincipleForm(forms.ModelForm):
    class Meta:
        model = ActivePrinciple
        fields = ['name', 'chemical_dosage']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'chemical_dosage': forms.TextInput(attrs={'class': 'form-control'}),
        }

# NOTE: Removed the 'prefix' argument here because inlineformset_factory does not support it.
ActivePrincipleFormSet = inlineformset_factory(
    Medication,
    ActivePrinciple,
    form=ActivePrincipleForm,
    extra=1,
    can_delete=True
)
