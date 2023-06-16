from django.urls import path
from .views import register, profile, edit_user


urlpatterns = [
    path('register/', register, name='register'),
    path('accounts/profile/', profile, name='profile'),
    path('edit/', edit_user, name='edit_user'),

    # Костыль :bone:
    path('', profile, name='main_page'),
]
