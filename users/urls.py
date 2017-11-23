from django.conf.urls import url

urlpatterns = [
    url(r'^all-users/$', 'users.views.all_users', name='all_users'),
   ]
