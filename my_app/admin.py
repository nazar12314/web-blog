from django.contrib import admin
from .models import Post, CustomUser, Comment
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm, CustomUserChangeForm


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'age', 'is_staff']


class CommentInline(admin.TabularInline):
    model = Comment


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Comment)
admin.site.register(Post, PostAdmin)
