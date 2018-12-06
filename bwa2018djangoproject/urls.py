"""bwa2018djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include, re_path
from user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.profile, name='home'),
    re_path(r'^login', views.login_user, name='login'),
    re_path(r'^logout', views.logout_user, name='logout'),
    re_path(r'^account_activation_sent/$', views.account_activation_sent,
            name='account_activation_sent'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            views.activate, name='activate'),
    path(r'oauth/', include('social_django.urls', namespace='social')),
    path(r'user/', include("user.urls")),
    path(r'friendship/', include("friendship.urls")),
    re_path(r'^discussions/', include("discussion.urls"))
]
