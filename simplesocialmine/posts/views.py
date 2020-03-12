from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from braces.views import SelectRelatedMixin
from django.views.generic import CreateView,UpdateView,ListView,DetailView

from posts import models,forms

class CreatePost(LoginRequiredMixin,SelectRelatedMixin,CreateView):
    model = models.Post
    fields = ('message','group')

# Create your views here.
