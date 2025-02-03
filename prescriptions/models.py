# prescriptions/models.py

from django.db import models
from patients.models import Patient
from django.urls import reverse

class Medication(models.Model):
    brand_name = models.CharField(max_length=100, help_text="e.g., Celexa")
    generic_name = models.CharField(max_length=100, help_text="e.g., citalopram")
    dosage_form = models.CharField(
        max_length=100,
        help_text="e.g., oral tablet (10 mg; 20 mg; 40 mg)"
    )
    drug_class = models.CharField(
        max_length=255,
        help_text="e.g., Selective serotonin reuptake inhibitor"
    )
    dosage_instructions = models.TextField(
        blank=True,
        null=True,
        help_text="Additional instructions if any."
    )

    def __str__(self):
        return self.brand_name

    def get_alternatives(self):
        """
        Returns other medications that share at least one active principle.
        (This is an example implementation.)
        """
        # Get the list of active principle names for this medication:
        my_active_names = self.active_principles.values_list('name', flat=True)
        return Medication.objects.filter(active_principles__name__in=my_active_names).exclude(pk=self.pk).distinct()

    def get_absolute_url(self):
        return reverse('medication_detail', kwargs={'pk': self.pk})


class ActivePrinciple(models.Model):
    medication = models.ForeignKey(
        Medication,
        on_delete=models.CASCADE,
        related_name='active_principles'
    )
    name = models.CharField(max_length=100, help_text="e.g., citalopram")
    chemical_dosage = models.CharField(max_length=50, help_text="e.g., 10 mg")

    def __str__(self):
        return f"{self.name} ({self.chemical_dosage})"


# The rest of your prescriptions models (Prescription, PrescriptionMedication, etc.)
# remain unchanged from the previous solution.
class Prescription(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name='prescriptions'
    )
    issued_date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    source_appointment = models.ForeignKey(
        'appointments.Appointment',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='prescriptions_created'
    )

    def __str__(self):
        return f"Prescription for {self.patient} on {self.issued_date}"

    def get_absolute_url(self):
        return reverse('prescription_detail', kwargs={'pk': self.pk})


class PrescriptionMedication(models.Model):
    prescription = models.ForeignKey(
        Prescription,
        on_delete=models.CASCADE,
        related_name='prescription_medications'
    )
    medication = models.ForeignKey(
        Medication,
        on_delete=models.CASCADE,
        related_name='prescription_medications'
    )
    dosage = models.CharField(max_length=100, blank=True, null=True)
    frequency = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.medication.brand_name} (dosage={self.dosage}, freq={self.frequency})"


class PrescriptionTemplate(models.Model):
    name = models.CharField(max_length=100)
    medications = models.ManyToManyField(Medication)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
