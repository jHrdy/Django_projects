from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView

from . import models
from . import forms
from .forms import NotesForm, AuthorForm

def index(request):

    context = {}
    context["authors_count"] = models.Author.objects.count()
    context["notes_count"] = models.Notes.objects.count()
    context["notes_list"] = models.Notes.objects.all().order_by('-id')

    return render(request, "noteapp/index.html", context)

def list_notes(request):
    notes = models.Notes.objects.all()
    return render(request, 'index.html', {'Notes': notes})

class NotesListView(ListView):
    model = models.Notes

class AuthorsListView(ListView):
    model = models.Author

def add_note(request):
    form_author = AuthorForm()
    if request.method == 'POST':
        form = NotesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            context = {'form' : form}
            return render(request, 'noteapp/add_note.html', context)
        
    context = {'form':NotesForm()}

    return render(request, 'noteapp/add_note.html', context)

def add_author(request):
    if request.method == 'POST':
        form_author = AuthorForm(request.POST)
        if form_author.is_valid():
            form_author.save()
        else:
            context = {'form_author': form_author}
            return render(request, 'noteapp/add_author.html', context)
    context = {'form_author':AuthorForm()}

    return render(request, 'noteapp/add_author.html', context)

    