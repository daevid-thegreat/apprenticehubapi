from django.urls import path
from opening.views import add_opening, get_my_openings


urlpatterns = [
    path('add-opening/', add_opening, name='add-opening'),
    path('get-my-openings/', get_my_openings, name='get-my-openings'),

]
