from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('artigo/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('novo_post/', AddPostView.as_view(), name="add-post"),
    path('artigo/editar/<int:pk>', UpdatePostView.as_view(), name="update-post")
]
