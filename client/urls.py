from django.urls import path
from .views import ClientCreateView, ClientListView, ClientDetailView, ProjectCreateView, UserProjectListView

urlpatterns = [
    path('clients/', ClientListView.as_view(), name='client-list'),
    path('clientscreate/', ClientCreateView.as_view(), name='client-create'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('clients/<int:client_id>/projects/', ProjectCreateView.as_view(), name='project-create'),
    path('projects/', UserProjectListView.as_view(), name='user-projects')
]
