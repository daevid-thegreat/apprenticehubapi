from django.urls import path
from opening.views import add_opening


urlpatterns = [
    path('add-opening/', add_opening, name='add-opening'),

]
