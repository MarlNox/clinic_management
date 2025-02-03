# notes/models.py

from django.db import models
from patients.models import Patient
from django.urls import reverse

class SOAPNote(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='soap_notes'
    )
    subjective = models.TextField()
    objective = models.TextField()
    assessment = models.TextField()
    plan = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SOAP Note for {self.patient} on {self.created_at}"

    def get_absolute_url(self):
        return reverse('soapnote_detail', kwargs={'pk': self.pk})


class StandardForm(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title


# New model for ad hoc notes
class AdHocNote(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='ad_hoc_notes'
    )
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"AdHocNote for {self.patient} @ {self.created_at:%Y-%m-%d %H:%M}"

    def get_absolute_url(self):
        # Optionally, define a URL for viewing a single ad hoc note if needed.
        return reverse('ad_hoc_note_detail', kwargs={'pk': self.pk})
