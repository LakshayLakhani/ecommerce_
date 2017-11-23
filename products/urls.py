from django.conf.urls import url
from products import views

urlpatterns = [
   url(r'home/$', views.home, name='kk'),
   url(r'all/$', views.all, name='all'),
   # url(r'(?P<slug>.*)/$', views.single, name='single_product'),
   # (?P<id>/d+) for only numbers
   url(r'(?P<slug>[\w-]+)/$', views.single, name='single_product'),

   ]
