from django.contrib.auth import logout
from django.urls import path
from users.views import register_user, login_user, logout_user, HomeView, DescriptionView, AboutView

urlpatterns = [
    path('login/', login_user, name='login'),
    path('register/', register_user, name='register'),
    path('logout/', logout_user, name='logout'),
    path('', HomeView.as_view(), name='home'),

    path('description/', DescriptionView.as_view(), name='description'),

    path('about/', AboutView.as_view(), name='about'),
]