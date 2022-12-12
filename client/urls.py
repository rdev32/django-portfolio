from django.urls import path
from django.contrib.auth.views import LoginView, logout_then_login
from client.views import IndexView, ManageView, load

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('manage/', ManageView.as_view(), name="manage"),
    path('manage/load', load, name="load"),
    path('accounts/login/', LoginView.as_view(), name="login"),
    path('logout/', logout_then_login, name="logout"),
]