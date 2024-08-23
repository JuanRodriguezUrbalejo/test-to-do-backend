from django.urls import path
from .views import TaskViewSet, ListViewSet

urlpatterns = [    
    #URL para las tareas
    path('tarea/lista/', TaskViewSet.as_view({'get':'list'})),
    path('tarea/crear/', TaskViewSet.as_view({'post':'create'})),
    path('tarea/<int:pk>/', TaskViewSet.as_view({'get':'retrieve','put':'partial_update','delete':'destroy'})),

    #URL para las listas
    path('lista/lista/', ListViewSet.as_view({'get':'list'})),
    path('lista/crear/', ListViewSet.as_view({'post':'create'})),
    path('lista/<int:pk>/', ListViewSet.as_view({'get':'retrieve','put':'partial_update','delete':'destroy'})),


    # URL para obtener una lista con todas sus tareas
    #path('lista/<int:pk>/tareas/', ListViewSet.as_view({'get': 'tasks'})),
]