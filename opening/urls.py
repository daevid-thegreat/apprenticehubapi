from django.urls import path
from opening.views import add_opening, get_my_openings, get_opening, get_openings, apply_opening, get_applications, get_my_applications, update_opening, add_apprentice, delete_apprentice, delete_opening, get_apprentices, get_application, respond_to_application


urlpatterns = [
    path('add-opening/', add_opening, name='add-opening'),
    path('get-my-openings/', get_my_openings, name='get-my-openings'),
    path('get-opening/<str:uid>/', get_opening, name='get-opening'),
    path('get-openings/', get_openings, name='get-openings'),
    path('apply-opening/<str:uid>/', apply_opening, name='apply-opening'),
    path('get-applications/', get_applications, name='get-applications'),
    path('get-application/<str:uid>/', get_application, name='get-application'),
    path('respond-to-application/<str:uid>/', respond_to_application, name='respond-to-application'),
    path('get-my-applications/', get_my_applications, name='get-my-applications'),
    path('update-opening/<str:uid>/', update_opening, name='update-opening'),
    path('add-apprentice/', add_apprentice, name='add-apprentice'),
    path('delete-apprentice/<int:pk>/', delete_apprentice, name='delete-apprentice'),
    path('delete-opening/<str:uid>/', delete_opening, name='delete-opening'),
    path('get-apprentices/', get_apprentices, name='get-apprentices'),


]
