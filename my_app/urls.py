from django.urls import path
from .views import (
    HomeView,
    PostsList,
    PostView,
    PostCreateView, 
    PostDeleteView, 
    PostUpdateView, 
    SignupView
    )


urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("posts/", PostsList.as_view(), name="posts"),
    path("posts/<int:pk>/", PostView.as_view(), name="post"),
    path("posts/create", PostCreateView.as_view(), name="create_post"),
    path("posts/delete/<int:pk>/", PostDeleteView.as_view(), name="delete"),
    path("posts/update/<int:pk>", PostUpdateView.as_view(), name="update"),
    path("accounts/signup/", SignupView.as_view(), name="signup")
]
