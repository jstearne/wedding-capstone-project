from typing import ClassVar
from django.shortcuts import render, redirect, reverse
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, CreateView, UpdateView, DeleteView
from .models import Post, Guest
# at top of file with other imports
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



# Create your views here.
class Home(TemplateView):
    template_name = "home.html"



class Signup(View):
        # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("guestbook")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)



class Login(TemplateView):
    template_name = "login.html"



@method_decorator(login_required, name='dispatch') # block access if not registered
class Accommodations(TemplateView): # good as is
    template_name = "accommodations.html"



@method_decorator(login_required, name='dispatch') # block access if not registered
class Schedule(TemplateView): #  good as is
    template_name = "schedule.html"



@method_decorator(login_required, name='dispatch') # block access if not registered
class Photos(TemplateView): # good as is
    template_name = "photos.html"



# Guestbook Views (post CRUD functionality)
@method_decorator(login_required, name='dispatch') # block access if not registered
class Guestbook(TemplateView): #needs to be refactored into CRUD
    template_name = "guestbook/guestbook.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context



class CreatePost(CreateView):
    model = Post
    fields = ["title", "body", "created_at", "image", "user"]
    template_name = "post_create.html"
    success_url = "/guestbook"



class UpdatePost(UpdateView):
    model = Post
    fields = ["title", "body", "created_at", "image", "user"]
    template_name = "post_update.html"
    success_url = "/guestbook"



# post_delete is a confirmation page!
class DeletePost(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = "/guestbook"


