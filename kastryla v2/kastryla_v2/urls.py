"""
Definition of urls for kastryla_v2.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    # Django URL pattern для страницы CITRUS
path('CITRUS/', views.CITRUS, name='CITRUS'),
path('order/', views.order, name='order'),
path('MEAT_GRINDER_FLEISCHWOLF/', views.MEAT_GRINDER_FLEISCHWOLF, name='MEAT_GRINDER_FLEISCHWOLF'),
path('NUT_TART/', views.NUT_TART, name='NUT_TART'),
path('ZERKIENERER_CHOPPER/', views.ZERKIENERER_CHOPPER, name='ZERKIENERER_CHOPPER'),
path('JUICE_EXTRACTOR/', views.JUICE_EXTRACTOR, name='JUICE_EXTRACTOR'),
path('MEAT_GRINDER_FLEISHWOLF_2/', views.MEAT_GRINDER_FLEISHWOLF_2, name='MEAT_GRINDER_FLEISHWOLF_2'),
]
