from django.urls import path, include

from . import views

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path("signup/", views.signup, name="signup"),
    path("registration/", include('dj_rest_auth.registration.urls')),
]