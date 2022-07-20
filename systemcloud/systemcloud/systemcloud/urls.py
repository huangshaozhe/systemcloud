"""systemcloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from systemyun import views
#from systemyun import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',include('systemyun.urls')),
    path('add_account/', views.add_account),
    path('del_account/', views.del_account),
    path('revise/', views.revise),
    path('purchase_admin/', views.purchase_admin),
    path('donate/', views.donate),
    path('human_services/',views.human_services),
    #path(r'db_handle', views.db_handle),
    path(r'login', views.login),
    #path(r'del_db', views.del_db),
    path(r'sign-up/', views.sign_up),
]
