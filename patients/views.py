# patients/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Patient
from .forms import PatientForm, MedicalHistoryForm, DocumentForm
from django.contrib import messages

@login_required
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/patient_list.html', {'patients': patients})

@login_required
def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    # Get the latest medical history if it exists:
    history_instance = patient.medical_histories.last() if patient.medical_histories.exists() else None
    history_form = MedicalHistoryForm(instance=history_instance)
    document_form = DocumentForm()
    return render(request, 'patients/patient_detail.html', {
        'patient': patient,
        'history_form': history_form,
        'document_form': document_form
    })

@login_required
def patient_create(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save()
            messages.success(request, "Patient created successfully.")
            return redirect('patient_detail', pk=patient.pk)
    else:
        form = PatientForm()
    return render(request, 'patients/patient_form.html', {'form': form})

@login_required
def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, "Patient updated successfully.")
            return redirect('patient_detail', pk=patient.pk)
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patients/patient_form.html', {'form': form})

@login_required
def add_medical_history(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        form = MedicalHistoryForm(request.POST)
        if form.is_valid():
            history = form.save(commit=False)
            history.patient = patient
            history.save()
            messages.success(request, "Medical history updated.")
    return redirect('patient_detail', pk=pk)

@login_required
def upload_document(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.patient = patient
            document.save()
            messages.success(request, "Document uploaded successfully.")
    return redirect('patient_detail', pk=pk)
