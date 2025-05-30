from hello import views
"""
URL configuration for gettingstarted project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

# from django.contrib import admins
from django.urls import path
from django.contrib import admin

import hello.views

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("account/<int:account_id>/", hello.views.account_detail, name="account_detail"),
    path("news/", hello.views.news_list, name="news_list"),
    path("news/<slug:slug>/", hello.views.news_article, name="news_article"),
    path('jobs/', views.jobs_list, name='jobs_list'),
    path('jobs/<str:job_id>/', views.job_detail, name='job_detail'),
    path('accounts/add/', views.add_account, name='add_account'),
    path("admin/", admin.site.urls)]    # https://docs.djangoproject.com/en/5.2/ref/contrib/admin/


