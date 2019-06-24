"""sampleproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from catalog.views import form_view,model_form,html_form,booksearch,deletebook,editbook

from home.views import home_view,home_copy,login,signup,carouselpage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('deletebook/<str:id>',deletebook),
    path('model/',model_form),
    path('editbook/<str:id>',editbook),
    path('',booksearch),
    path('html/',html_form),
    #path('',home_view),
    path('homecopy',home_copy),
    path('login',login),
    path('signup',signup),
    path('carousel',carouselpage),
    path('form/',form_view)
]