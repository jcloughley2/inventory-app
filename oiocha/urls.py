from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from collection import views
from django.contrib.auth.views import(
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from collection.backends import MyRegistrationView
from django.views.generic import ListView, TemplateView, RedirectView
from django.urls import path
from collection.views import Home, ListCreate, ListDetail, ListUpdate

urlpatterns = [
    path('',Home.as_view(template_name='index.html'),name='home'),
    path('accounts/create_list/', ListCreate.as_view(template_name='lists/create_list.html'), name='registration_create_list'),
    path('lists/<slug>/', ListDetail.as_view(template_name='lists/list_detail.html'), name='list_detail'),
    path('lists/<slug>/edit/', ListUpdate.as_view(template_name='lists/create_list.html'), name='edit_list'),
    path('about/',TemplateView.as_view(template_name='about.html'),name='about'),
    path('contact/',TemplateView.as_view(template_name='contact.html'),name='contact'),
    path('accounts/password/reset/',PasswordResetView.as_view(),name="password_reset"),
    path('accounts/password/reset/done/',PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('accounts/password/reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('accounts/password/done',PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    path('accounts/register/',MyRegistrationView.as_view(),name='registration_register'),
    path('accounts/',include('registration.backends.default.urls')),
    path('admin/', admin.site.urls),
    path('browse/name/',views.browse_by_name, name='browse'),
    path('browse/name/<initial>/',views.browse_by_name, name='browse_by_name'),
    path('browse/', RedirectView.as_view(pattern_name='browse', permanent=True)),
    path('lists/', RedirectView.as_view(
        pattern_name='browse', permanent=True)),
    path('lists/<slug>/',
        views.ListDetail, name='list_detail'),
    path('lists/<slug>/edit/',
        views.edit_list, name='edit_list'),
]


