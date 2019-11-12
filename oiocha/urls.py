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

urlpatterns = [
    path('', views.index, name='home'),
    path('about/',TemplateView.as_view(template_name='about.html'),name='about'),
    path('contact/',TemplateView.as_view(template_name='contact.html'),name='contact'),
    path('lists/<slug>/', views.list_detail,name='list_detail'),
    path('lists/<slug>/edit/', views.edit_list,name='edit_list'),
    path('accounts/password/reset/',PasswordResetView.as_view(),name="password_reset"),
    path('accounts/password/reset/done/',PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('accounts/password/reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('accounts/password/done',PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    path('accounts/register/',MyRegistrationView.as_view(),name='registration_register'),
    path('accounts/create_list/', views.create_list,name='registration_create_list'),
    path('accounts/',include('registration.backends.default.urls')),
    path('admin/', admin.site.urls),
]
