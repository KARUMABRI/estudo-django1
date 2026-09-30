from django.urls import path
from recipes.views import home, contato, sobre



urlpatterns = [ #serve para mapear as urls para as views
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato)
    
]