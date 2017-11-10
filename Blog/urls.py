"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login

from blogs import views
from users import views as users_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^new_post/$', views.new_post, name='new_post'),
    url(r'^edit_post/(?P<post_id>\d+)/$', views.edit_post, name='edit_post'),
    url(r'^login/', login, {'template_name': 'users/login.html'}, name='login'),
    url(r'^logout/$', users_views.logout_view, name='logout'),
    url(r'^register/$', users_views.register, name='register'),
    ]
