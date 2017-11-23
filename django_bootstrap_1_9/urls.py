"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include

from django.contrib import admin
from django.contrib.auth import views
from django.views.static import serve
from django.conf import settings


from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^', TemplateView.as_view(template_name='home.html')),
    url(r'^users/', include('users.urls')),
    url(r'^products/', include('products.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {"document_root": settings.MEDIA_ROOT})
]
