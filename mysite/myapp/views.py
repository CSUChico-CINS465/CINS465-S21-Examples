from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout

from . import models
from . import forms

def logout_view(request):
    logout(request)
    return redirect("/login/")


# Create your views here.
def index(request):
    if request.method == "POST":
        suggestion_form = forms.SuggestionForm(request.POST)
        if suggestion_form.is_valid():
            suggestion_form.save(request)
            suggestion_form = forms.SuggestionForm()
    else:
        suggestion_form = forms.SuggestionForm()
    suggestion_objects = models.SuggestionModel.objects.all()
    suggestion_list = []
    for sugg in suggestion_objects:
        comment_objects = models.CommentModel.objects.filter(suggestion=sugg)
        temp_sugg = {}
        temp_sugg["suggestion"] = sugg.suggestion
        temp_sugg["id"] = sugg.id
        temp_sugg["author"] = sugg.author.username
        temp_sugg["comments"] = comment_objects
        suggestion_list += [temp_sugg]
    context = {
        "title":"CINS 465 Title",
        "variable": "Awesome Template",
        "suggestions":suggestion_list,
        "suggestion_form":suggestion_form,
    }
    return render(request, "index.html", context=context)
    # return HttpResponse("Hello World")

def register_view(request):
    if request.method == "POST":
        form_instance = forms.RegistrationForm(request.POST)
        if form_instance.is_valid():
            user = form_instance.save()
            #authenticate the user
            return redirect("/login/")
    else:
        form_instance = forms.RegistrationForm()
    
    context = {
        "title":"Registration",
        "form":form_instance
    }
    return render(request, "registration/register.html", context=context)