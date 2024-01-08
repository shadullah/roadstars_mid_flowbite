from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register,name='register'),
    # path('login/', views.userLogin,name='login'),
    path('login/', views.UserLoginView.as_view(),name='login'),
    path('logout/', views.user_logout,name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit_profile/', views.editProfile, name='edit_profile'),
]
