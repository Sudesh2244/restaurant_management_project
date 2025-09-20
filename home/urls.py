from django.urls import path
 
from rest_framework.authtoken.views import obtain_auth_token
from . import views
urlpatterns = [

    
    path('', views.home, name='home'),
    path('notes/', views.note_list, name='note_list'),
    path('notes/list/', views.NoteListView.as_view(), name='note_list_view'),
    path('api/notes/', views.NoteViewSet.as_view({'get': 'list', 'post': 'create'}), name='api_notes'),
    path('api/notes/<int:pk>/', views.NoteViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='api_note_detail'),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
    

]
