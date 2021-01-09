from django.urls import path
from . import views
app_name = 'drug'
urlpatterns = [
    path('list/', views.DrugListView.as_view(),
         name='drug_list'),
    path('create/', views.DrugCreateView.as_view(),
         name='drug_create'),
    path('update/<int:pk>', views.DrugUpdateView.as_view(),
         name='drug_update'),
    path('delete/<int:pk>', views.DrugDeleteView.as_view(),
         name='drug_delete'),

]
