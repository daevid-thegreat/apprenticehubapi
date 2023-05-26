from django.urls import path
from opening.views import add_opening


urlpatterns = [
    path('add-opeining/', add_opening, name='add-opening'),

]
