from django.urls import path

from users.views import register_view, login_view, logout_view, profile_view, profile_edit

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile_view'),
    path('profile/edit/', profile_edit, name='profile_edit'),
]