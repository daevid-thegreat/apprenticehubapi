from django.urls import path
from authent.views import signup, signup_master, check_auth, signin, verify_email, resend_email_otp, change_password, update_user, getCompany, addCompany, updateCompany, reset_password
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('check-auth/', check_auth, name='check-auth'),

    path('signup/', signup, name='signup'),

    path('verify-mail/', verify_email, name='verify-mail'),
    path('resend_otp/', resend_email_otp, name='resend_otp'),
    path('signin/', signin, name='signin'),
    path('change-password/', change_password, name='change-password'),
    path('update-profile/', update_user, name='update-profile'),
    path('new-password/', reset_password, name='reset-password'),


    path('signup-master/', signup_master, name='signup-master'),
    path('get-company/', getCompany, name='get-company'),
    path('add-company/', addCompany, name='add-company'),
    path('update-company/', updateCompany, name='update-company'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
