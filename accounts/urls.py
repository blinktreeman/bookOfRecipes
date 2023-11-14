from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # https://docs.djangoproject.com/en/4.2/topics/auth/default/#module-django.contrib.auth.views
    # login/logout
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # change pass
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # reset pass
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # register new user, edit profile
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('edit-profile/', views.EditUserProfile.as_view(), name='edit_profile')
]
