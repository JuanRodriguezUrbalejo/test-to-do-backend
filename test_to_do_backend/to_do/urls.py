from django.urls import path
from .views import TaskViewSet, ListViewSet

urlpatterns = [
    path('tarea/lista/', TaskViewSet.as_view({'get':'list'})),
    path('tarea/crear/', TaskViewSet.as_view({'post':'create'})),
    path('tarea/<int:pk>/', TaskViewSet.as_view({'get':'retrieve','put':'partial_update','delete':'destroy'})),

    path('lista/lista/', ListViewSet.as_view({'get':'list'})),
    path('lista/crear/', ListViewSet.as_view({'post':'create'})),
    path('lista/<int:pk>/', ListViewSet.as_view({'get':'retrieve','put':'partial_update','delete':'destroy'})),
]