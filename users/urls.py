from django.urls import path, include
from .views import DashBoardView, SignUpView

urlpatterns = [
    path('', DashBoardView.as_view(), name="dashboard"),
    path('', include("django.contrib.auth.urls")),
    path('signup', SignUpView.as_view(), name="signup"),
]