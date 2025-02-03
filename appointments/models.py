# appointments/models.py

from django.db import models
from django.urls import reverse
from patients.models import Patient

class Appointment(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='appointments'
    )
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    notes = models.TextField(blank=True, null=True)
    is_recurring = models.BooleanField(default=False)
    # Fields for post-appointment management:
    doctor_notes = models.TextField(blank=True, null=True)
    updated_diagnosis = models.TextField(blank=True, null=True)
    # Even though we changed prescription handling later, we can keep this for legacy purposes.
    # (It is referenced in appointment_manage in our views.)
    updated_medications = models.ManyToManyField(
        'prescriptions.Medication',
        blank=True,
        related_name='appointment_updates'
    )
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Appointment with {self.patient} on {self.date}"

    def get_absolute_url(self):
        return reverse('appointment_detail', kwargs={'pk': self.pk})
