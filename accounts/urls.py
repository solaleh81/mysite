from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    # logout
    path('logout/', views.logout_view, name='logout'),
    # signup
    path('signup/', views.signup_view, name='signup'),
]
