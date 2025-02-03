# notes/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import SOAPNote, AdHocNote
from .forms import SOAPNoteForm, AdHocNoteForm

@login_required
def soapnote_list(request):
    notes = SOAPNote.objects.all().order_by('-created_at')
    return render(request, 'notes/soapnote_list.html', {'notes': notes})

@login_required
def soapnote_create(request):
    if request.method == "POST":
        form = SOAPNoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "SOAP Note created successfully.")
            return redirect('soapnote_list')
    else:
        form = SOAPNoteForm()
    return render(request, 'notes/soapnote_form.html', {'form': form})


################################################################
# New view for Ad-Hoc Note creation
################################################################
@login_required
def ad_hoc_note_create(request):
    if request.method == "POST":
        form = AdHocNoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ad hoc note created successfully.")
            # Optionally redirect to the patient detail if you want:
            patient_id = form.cleaned_data['patient'].id
            return redirect('patient_detail', pk=patient_id)
    else:
        form = AdHocNoteForm()
    return render(request, 'notes/ad_hoc_note_form.html', {'form': form})
