from django import forms
from .models import Post, Category


class CategoryForm(forms.ModelForm):
    name = forms.CharField(
        label="Nome", widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Category
        fields = ('name', )


class PostForm(forms.ModelForm):
    choices = Category.objects.all().values_list('name', 'name')
    title = forms.CharField(
        max_length=100,
        label="Título",
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.CharField(label="Categoria",
                               widget=forms.Select(
                                   choices=choices,
                                   attrs={'class': 'form-control'}))
    body = forms.CharField(
        label="Texto", widget=forms.Textarea(attrs={'class': 'form-control'}))
    snippet = forms.CharField(label="Resumo",
                              widget=forms.Textarea(attrs={
                                  'rows': '5',
                                  'class': 'form-control'
                              }))
    header_image = forms.ImageField(
        label="Imagem",
        widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'body', 'snippet',
                  'header_image')
        widgets = {
            'author':
            forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'author',
                'type': 'hidden'
            })
        }