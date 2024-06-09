from django.urls import path
from . import views

app_name = 'artigos'

urlpatterns = [
    path('', views.index_view, name='index_view'),
    path('<int:artigo_id>/', views.detail_view, name='detail_view'),

]
