"""webapps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from myblog import views
from django.conf import settings
urlpatterns = [
    path('', views.about_me_action, name='home'),
    path('post_page/<int:postID>', views.view_post_action, name='post'),
    path('filter_post/<int:tagID>', views.filter_post_action, name='filter_post'),
    path('posts/', views.view_all_posts_action, name='blog'),
    path('about_me/', views.about_me_action, name='about_me'),
    path('admin/', admin.site.urls, name='admin'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
