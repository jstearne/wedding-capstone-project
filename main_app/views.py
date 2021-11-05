from typing import ClassVar
from django.shortcuts import render, redirect, reverse
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
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
class Guestbook(TemplateView):
    template_name = "guestbook/guestbook.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name != None:
            context["posts"] = Post.objects.filter(name__icontains=name) 
            # context["header"] = f"Searching for \"{name}\"" 
        else:
            context["posts"] = Post.objects.all()
            # context["header"] = "Dogs!"
        return context



class CreatePost(CreateView):
    model = Post
    fields = ["title", "body", "image"] # no option to select user!
    template_name = "guestbook/post_create.html"
    success_url = "/guestbook"

    def form_valid(self, form): # make sure posts are saving who posted!
        form.instance.user = self.request.user
        return super(CreatePost, self).form_valid(form)


class UpdatePost(UpdateView):
    model = Post
    fields = ["title", "body", "image"]
    template_name = "post_update.html"
    success_url = "/guestbook"



# post_delete is a confirmation page!
class DeletePost(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = "/guestbook"


