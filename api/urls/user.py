from django.urls import path

from api.view.user import UserListAPIView, UserRetrieveUpdateAPIView

app_name = "api"

urlpatterns = [
    path("", UserListAPIView.as_view(), name="list"),
    path("<int:pk>/", UserRetrieveUpdateAPIView.as_view(), name="detail"),
]
