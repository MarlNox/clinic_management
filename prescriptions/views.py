# prescriptions/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Prescription, Medication
from .forms import PrescriptionForm, MedicationForm
from django.contrib import messages

@login_required
def prescription_list(request):
    prescriptions = Prescription.objects.all().order_by('-issued_date')
    return render(request, 'prescriptions/prescription_list.html', {'prescriptions': prescriptions})

@login_required
def prescription_create(request):
    if request.method == "POST":
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Prescription created successfully.")
            return redirect('prescription_list')
    else:
        form = PrescriptionForm()
    return render(request, 'prescriptions/prescription_form.html', {'form': form})

@login_required
def medication_list(request):
    medications = Medication.objects.all()
    return render(request, 'prescriptions/medication_list.html', {'medications': medications})

@login_required
def medication_create(request):
    if request.method == "POST":
        form = MedicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Medication created successfully.")
            return redirect('medication_list')
    else:
        form = MedicationForm()
    return render(request, 'prescriptions/medication_form.html', {'form': form})
