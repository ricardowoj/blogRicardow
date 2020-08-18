from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, AddCategoryView, UpdatePostView, DeletePostView, CategoryView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('artigo/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('novo_post/', AddPostView.as_view(), name="add-post"),
    path('nova_categoria/', AddCategoryView.as_view(), name="add-category"),
    path('artigo/editar/<int:pk>', UpdatePostView.as_view(), name="update-post"),
    path('artigo/deletar/<int:pk>', DeletePostView.as_view(), name="delete-post"),
    path('category/<str:category>/', CategoryView, name='category')
]
