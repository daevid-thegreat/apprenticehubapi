from django.urls import path
from authent.views import signup, signup_master, check_auth, signin, verify_email


urlpatterns = [
    path('check-auth/', check_auth, name='check-auth'),

    path('signup/', signup, name='signup'),
    path('verify-mail/', verify_email, name='verify-mail'),
    path('signin/', signin, name='signin'),

    path('signup_master/', signup_master, name='signup-master'),
]