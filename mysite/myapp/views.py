from django.shortcuts import render
from django.http import HttpResponse

from . import models

# Create your views here.
def index(request):
    suggestion_objects = models.SuggestionModel.objects.all()
    context = {
        "title":"CINS 465 Title",
        "variable": "Awesome Template",
        "suggestions":suggestion_objects,
    }
    return render(request, "index.html", context=context)
    # return HttpResponse("Hello World")