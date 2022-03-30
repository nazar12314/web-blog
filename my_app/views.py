from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import (
    UpdateView,
    CreateView,
    DeleteView
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from .models import Post
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'


class PostsList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts.html'
    login_url = 'login'


class PostView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post.html'
    login_url = 'login'


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['heading', 'text']
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy("posts")
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "create_post.html"
    fields = ['heading', 'text']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class SignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
