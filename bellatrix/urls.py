from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_wand, name='all_wand'),
    path('wand_stores/', views.wand_store_view, name='wand_stores'),
    path('<int:wand_id>/', views.wand_detail, name='wand_detail'),
]
