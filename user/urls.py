from django.urls import path

from user.views import UserSignInView, UserLogoutView, UserSignUpView, UserProfileView

urlpatterns = [
    path('login/', UserSignInView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserSignUpView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]
