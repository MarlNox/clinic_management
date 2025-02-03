# reports/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from patients.models import Patient
from appointments.models import Appointment
from prescriptions.models import Prescription

@login_required
def practice_report(request):
    total_patients = Patient.objects.count()
    total_appointments = Appointment.objects.count()
    total_prescriptions = Prescription.objects.count()
    context = {
        'total_patients': total_patients,
        'total_appointments': total_appointments,
        'total_prescriptions': total_prescriptions,
    }
    return render(request, 'reports/report.html', context)
