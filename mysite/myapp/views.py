from django.shortcuts import render
from django.http import HttpResponse

from . import models
from . import forms

# Create your views here.
def index(request):
    if request.method == "POST":
        suggestion_form = forms.SuggestionForm(request.POST)
        if suggestion_form.is_valid():
            suggestion_form.save()
            suggestion_form = forms.SuggestionForm()
    else:
        suggestion_form = forms.SuggestionForm()
    suggestion_objects = models.SuggestionModel.objects.all()
    context = {
        "title":"CINS 465 Title",
        "variable": "Awesome Template",
        "suggestions":suggestion_objects,
        "suggestion_form":suggestion_form,
    }
    return render(request, "index.html", context=context)
    # return HttpResponse("Hello World")