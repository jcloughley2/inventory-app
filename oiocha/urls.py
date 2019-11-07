from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from collection import views
from django.contrib.auth.views import (
   password_reset,
   password_reset_done,
   password_reset_confirm,
   password_reset_complete
)

urlpatterns = [
    path('', views.index, name='home'),
    # The new URL entries we're adding:
    path('about/',
        TemplateView.as_view(template_name='about.html'),
        name='about'),
    path('contact/',
        TemplateView.as_view(template_name='contact.html'),
        name='contact'),
    path('lists/<slug>/', views.list_detail,
        name='list_detail'),
    path('lists/<slug>/edit/', views.edit_list,
        name='edit_list'),
    path('admin/', admin.site.urls),
    path('accounts/',
        include('registration.backends.simple.urls')),
    path('admin/', admin.site.urls),
    path('accounts/password/reset/',
        password_reset,
        {'template_name':
        'registration/password_reset_form.html'},
        name="password_reset"),
    path('accounts/password/reset/done/',
        password_reset_done,
        {'template_name':
        'registration/password_reset_done.html'},
        name="password_reset_done"),
    path('accounts/password/reset/<uidb64>/<token>/',
        password_reset_confirm,
        {'template_name':
        'registration/password_reset_confirm.html'},
        name="password_reset_confirm"),
    path('accounts/password/done/',
        password_reset_complete,
        {'template_name':
        'registration/password_reset_complete.html'},
        name="password_reset_complete"),
    path('accounts/',
        include('registration.backends.simple.urls')),
    path('admin/', admin.site.urls),
]