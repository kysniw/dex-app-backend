from django.urls import path

from user import views


app_name = 'user'

urlpatterns = [
    path('manage/', views.CreateUserView.as_view(), name='manage'),
    path('change_password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
]
