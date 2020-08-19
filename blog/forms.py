from django import forms
from .models import Post, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control'})
        }


class PostForm(forms.ModelForm):
    class Meta:
        choices = Category.objects.all().values_list('name', 'name')
        model = Post
        fields = ('title', 'author', 'category', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'author', 'type': 'hidden'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }
