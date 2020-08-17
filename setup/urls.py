from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('usuario/', include('django.contrib.auth.urls')),
    path('usuario/', include('members.urls')),
]
