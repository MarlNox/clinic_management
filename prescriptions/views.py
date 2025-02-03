# prescriptions/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Prescription
from .forms import PrescriptionForm
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
