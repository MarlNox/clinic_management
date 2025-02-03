# notes/forms.py
from django import forms
from .models import SOAPNote

class SOAPNoteForm(forms.ModelForm):
    class Meta:
        model = SOAPNote
        fields = ['patient', 'subjective', 'objective', 'assessment', 'plan']
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'subjective': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'objective': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'assessment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'plan': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
