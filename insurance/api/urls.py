from django.urls import path
from . import views
app_name = 'insurance_api'
urlpatterns = [
    path('regions/', views.RegionListView.as_view(),
         name='region_list'),
    path('regions/<pk>/', views.RegionDetailView.as_view(),
         name='region_detail'),
]
