# appointments/forms.py
from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'date', 'start_time', 'end_time', 'notes', 'is_recurring']
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'end_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'is_recurring': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

# NEW: Form for managing (post-appointment) updates
class AppointmentManageForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor_notes', 'updated_diagnosis', 'updated_medications', 'is_completed']
        widgets = {
            'doctor_notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'updated_diagnosis': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'updated_medications': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'is_completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
