"""mimmit_koodaa_todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.views import serve
from django.urls import path, include
from rest_framework import routers

from todo import viewsets as todo_viewsets

router = routers.DefaultRouter()
router.register(r'todo', todo_viewsets.TodoViewSet, basename = 'todo')
router.register(r'category', todo_viewsets.CategoryViewSet, basename = 'category')
# Register view sets here

urlpatterns = [
    path('v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^$', serve, kwargs={'path': 'index.html'}),
    url(r'^favicon.ico$', serve, kwargs={'path': 'favicon.ico'}),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)