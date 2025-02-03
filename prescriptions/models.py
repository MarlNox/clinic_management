# prescriptions/models.py
from django.db import models
from patients.models import Patient
from django.urls import reverse

class Medication(models.Model):
    name = models.CharField(max_length=100)
    dosage_instructions = models.TextField()

    def __str__(self):
        return self.name

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='prescriptions')
    medications = models.ManyToManyField(Medication)
    issued_date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    # New field to track if the prescription was updated via an appointment:
    source_appointment = models.ForeignKey('appointments.Appointment', null=True, blank=True, on_delete=models.SET_NULL, related_name='prescriptions_created')

    def __str__(self):
        return f"Prescription for {self.patient} on {self.issued_date}"

    def get_absolute_url(self):
        return reverse('prescription_detail', kwargs={'pk': self.pk})

class PrescriptionTemplate(models.Model):
    name = models.CharField(max_length=100)
    medications = models.ManyToManyField(Medication)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
