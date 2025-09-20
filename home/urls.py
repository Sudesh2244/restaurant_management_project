from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
import home
urlpatterns = [

    
    path('', home.home, name='home'),
    path('notes/', home.note_list, name='note_list'),
    path('notes/list/', home.NoteListView.as_view(), name='note_list_view'),
    path('api/notes/', home.NoteViewSet.as_view({'get': 'list', 'post': 'create'}), name='api_notes'),
    path('api/notes/<int:pk>/', home.NoteViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='api_note_detail'),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
    

]
