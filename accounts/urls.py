
from django.urls import path
from .views import RegisterView, LoginView, LogoutView, UserProfileView

urlpatterns = [
    path('api/accounts/', RegisterView.as_view(), name='register'),
    path('api/accounts/login/', LoginView.as_view(), name='login'),
    path('api/accounts/logout/', LogoutView.as_view(), name='logout'),
    path('api/accounts/<str:username>/',
         UserProfileView.as_view(), name='user-profile'),
]
