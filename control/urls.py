from django.urls import path
from django.contrib.auth.views import LoginView, logout_then_login
from control.views import ControlView, gh_loader

urlpatterns = [
    path('control/', ControlView.as_view(), name='control'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('logout/', logout_then_login, name='logout'),
    path('load/', gh_loader, name='load')
]