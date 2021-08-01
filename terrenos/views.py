from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def homepage(request, template_name="base.html"):
    return render(request, template_name)
