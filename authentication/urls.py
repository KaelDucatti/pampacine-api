from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatters = [
    path(
        "authentication/token/",
        TokenObtainPairView.as_view(),
        name="get-obtain-pair",
    )
]
