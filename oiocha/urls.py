from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from collection import views

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
]