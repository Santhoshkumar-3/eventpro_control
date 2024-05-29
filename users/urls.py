from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserProfileView, ChangePasswordView, StudentUserList, StaffUserList

urlpatterns = [
    path('auth/register/', UserRegistrationView.as_view(), name='user_registration'),
    path('auth/login/', UserLoginView.as_view(), name='user_login'),
    path('users/profile/<int:pk>/', UserProfileView.as_view(), name='user_profile'),
    path('users/change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('students/', StudentUserList.as_view(), name='student-list'),
    path('staff/', StaffUserList.as_view(), name='staff-list'),
]
