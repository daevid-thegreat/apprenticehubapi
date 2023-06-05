from django.urls import path
from opening.views import add_opening, get_my_openings, get_opening, get_openings, apply_opening, get_applications, get_my_applications


urlpatterns = [
    path('add-opening/', add_opening, name='add-opening'),
    path('get-my-openings/', get_my_openings, name='get-my-openings'),
    path('get-opening/<str:uid>/', get_opening, name='get-opening'),
    path('get-openings/', get_openings, name='get-openings'),
    path('apply-opening/<str:uid>/', apply_opening, name='apply-opening'),
    path('get-applications/', get_applications, name='get-applications'),

]
