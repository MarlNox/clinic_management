# appointments/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Appointment
from .forms import AppointmentForm
from django.contrib import messages
import datetime

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
    # For demonstration, show appointments for the current month.
    today = datetime.date.today()
    appointments = Appointment.objects.filter(date__month=today.month, date__year=today.year)
    return render(request, 'appointments/appointment_calendar.html', {'appointments': appointments})
