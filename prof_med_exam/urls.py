from django.urls import path
from . import views
app_name = 'prof_med_exam'
urlpatterns = [
    path('harm/list/', views.HarmListView.as_view(),
         name='harm_list'),
    path('harm/create/', views.HarmCreateView.as_view(),
         name='harm_create'),
    path('harm/update/<int:pk>', views.HarmUpdateView.as_view(),
         name='harm_update'),
    path('harm/delete/<int:pk>', views.HarmDeleteView.as_view(),
         name='harm_delete'),
]
