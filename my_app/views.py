from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Post
from django.urls import reverse_lazy


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'


class PostsList(ListView):
    model = Post
    template_name = 'posts.html'


class PostView(DetailView):
    model = Post
    template_name = 'post.html'


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['heading', 'text']


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy("posts")


class PostCreateView(CreateView):
    model = Post
    template_name = "create_post.html"
    fields = ['heading', 'text']


class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
