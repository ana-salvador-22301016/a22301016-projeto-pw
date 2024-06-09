from django.urls import path
from .views import intro_view,mebyme_detail,tech_presentation,allApp_view,video

urlpatterns = [
    path('', intro_view, name='intro_view'),
    path('mebyme/', mebyme_detail, name='mebyme_detail'),
    path('TechIntro/', tech_presentation, name='tech_presentation'),
    path('allApp/',allApp_view,name = 'allAppview'),
    path('video/',video,name = 'video'),


    # Other URL patterns...
]
