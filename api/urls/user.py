from django.urls import path

from api.view.user import UserRetrieveAPIView, UserListAPIView, UserProfileRetrieveAPIView

app_name = "api"

urlpatterns = [
    path("profile/<int:pk>/", UserProfileRetrieveAPIView.as_view(), name="profile_detail"),
    path("", UserListAPIView.as_view(), name="list"),
    path("<int:pk>/", UserRetrieveAPIView.as_view(), name="detail"),
]
