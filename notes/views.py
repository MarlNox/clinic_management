# notes/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SOAPNote
from .forms import SOAPNoteForm
from django.contrib import messages

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
