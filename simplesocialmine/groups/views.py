from django.shortcuts import render
from django.views.generic import CreateView,DetailView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from groups.models import Group,GroupMember

# Create your views here.
class CreateGroup(LoginRequiredMixin,CreateView):
    model = Group
    fields = ('name','description')

class SingleGroup(DetailView):
    model = Group

class ListGroup(ListView):
    model = Group
