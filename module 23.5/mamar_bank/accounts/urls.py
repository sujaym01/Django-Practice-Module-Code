from django.urls import path
from .views import (UserRegistrationView, UserLoginView, UserLogoutView,
            UserBankAccountUpdateView,UserProfileView,UserPasswordChangeView)
 
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('update_profile/', UserBankAccountUpdateView.as_view(), name='update_profile'),
    path('password_change/', UserPasswordChangeView.as_view(), name='password_change_done')
]