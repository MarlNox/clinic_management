# prescriptions/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Prescription, Medication
from .forms import (
    PrescriptionForm, 
    MedicationForm,
    PrescriptionMedicationFormSet,  # for multiple meds in a prescription
    ActivePrincipleFormSet          # only if you are using the advanced medication logic
)

@login_required
def prescription_list(request):
    prescriptions = Prescription.objects.all().order_by('-issued_date')
    return render(request, 'prescriptions/prescription_list.html', {'prescriptions': prescriptions})

@login_required
def prescription_create(request):
    """
    Create a Prescription along with multiple PrescriptionMedication entries via formset.
    """
    if request.method == "POST":
        prescription_form = PrescriptionForm(request.POST)
        formset = PrescriptionMedicationFormSet(request.POST)
        if prescription_form.is_valid() and formset.is_valid():
            prescription = prescription_form.save(commit=True)
            # Assign bridging objects to that prescription
            pm_objects = formset.save(commit=False)
            for pm in pm_objects:
                pm.prescription = prescription
                pm.save()
            # Handle deleted forms
            for deleted in formset.deleted_objects:
                deleted.delete()

            messages.success(request, "Prescription created successfully.")
            return redirect('prescription_list')
    else:
        prescription_form = PrescriptionForm()
        formset = PrescriptionMedicationFormSet()

    return render(
        request,
        'prescriptions/prescription_form.html',
        {
            'prescription_form': prescription_form,
            'formset': formset,
        }
    )

@login_required
def medication_list(request):
    medications = Medication.objects.all()
    return render(request, 'prescriptions/medication_list.html', {'medications': medications})

@login_required
def medication_create(request):
    """
    Create a Medication record along with ActivePrinciples.
    """
    if request.method == "POST":
        form = MedicationForm(request.POST)
        formset = ActivePrincipleFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            medication = form.save()
            active_principles = formset.save(commit=False)
            for ap in active_principles:
                ap.medication = medication
                ap.save()
            messages.success(request, "Medication created successfully.")
            return redirect('medication_list')
    else:
        form = MedicationForm()
        formset = ActivePrincipleFormSet()

    return render(
        request,
        'prescriptions/medication_form.html',
        {
            'form': form,
            'formset': formset
        }
    )
