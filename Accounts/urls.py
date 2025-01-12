from django.urls import path
from . import views

urlpatterns = [
    path('account/sign_up', views.AccountSignUp, name='Sign Up'),
    path('account/sign_in', views.AccountSignIn, name='Sign In'),
    path('account/sign_out', views.AccountSignOut, name='Sign Out'),
    path('account/view', views.AccountView, name='Account'),
    path('account/delete', views.AccountDelete, name='Delete Account'),
]