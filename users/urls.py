from django.urls import path, include, re_path
from dj_rest_auth.registration.views import VerifyEmailView, RegisterView
from .views import ( userDelete, ConfirmEmailView )

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path("registration/", include('dj_rest_auth.registration.urls')),
    path('delete/<int:id>/', userDelete, name="user_delete"),
    re_path(r'^account-confirm-email/$', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),
]