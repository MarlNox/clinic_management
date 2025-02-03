# appointments/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Appointment
from .forms import AppointmentForm, AppointmentManageForm
from django.contrib import messages

@login_required
def appointment_list(request):
    appointments = Appointment.objects.all().order_by('date', 'start_time')
    return render(request, 'appointments/appointment_list.html', {'appointments': appointments})

@login_required
def appointment_create(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Appointment scheduled successfully.")
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/appointment_form.html', {'form': form})

@login_required
def appointment_calendar(request):
    appointments = Appointment.objects.all().order_by('date', 'start_time')
    return render(request, 'appointments/appointment_calendar.html', {'appointments': appointments})

@login_required
def appointment_manage(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == "POST":
        form = AppointmentManageForm(request.POST, instance=appointment)
        if form.is_valid():
            appointment = form.save()
            # Update patient current diagnosis if provided
            if appointment.updated_diagnosis:
                patient = appointment.patient
                patient.current_diagnosis = appointment.updated_diagnosis
                patient.save()
            # If updated medications were selected, create a new Prescription record.
            if appointment.updated_medications.exists():
                from prescriptions.models import Prescription, PrescriptionMedication
                prescription = Prescription.objects.create(
                    patient=appointment.patient,
                    source_appointment=appointment,
                )
                # Create bridging objects for each updated medication
                for med in appointment.updated_medications.all():
                    PrescriptionMedication.objects.create(
                        prescription=prescription,
                        medication=med,
                        dosage="(Not specified)",
                        frequency="(Not specified)"
                    )
                prescription.save()

            messages.success(request, "Appointment updated successfully.")
            return redirect('appointment_list')
    else:
        form = AppointmentManageForm(instance=appointment)

    return render(request, 'appointments/appointment_manage.html', {
        'form': form,
        'appointment': appointment
    })
