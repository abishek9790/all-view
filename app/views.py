from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.
class home(TemplateView):
    template_name='app/home.html'

class schoollist(ListView):
    model=school
    context_object_name='schools'
    ordering=['name']


class schooldetail(DetailView):
    model=school
    context_object_name='sc'

class schoolcreate(CreateView):
    model=school
    fields='__all__'

class schoolupdate(UpdateView):
    model=school
    fields='__all__'
class schooldelete(DeleteView):
    model=school
    context_object_name='sc'
    success_url=reverse_lazy('schoollist')