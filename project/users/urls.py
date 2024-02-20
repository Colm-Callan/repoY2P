from django.urls import path
from .views import SignUpView, HomePageView, UserProfileView

urlpatterns =[
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', HomePageView.as_view(), name='home'),
    path('<int:pk>/', UserProfileView.as_view(), name='user_profile'),
    
    ]