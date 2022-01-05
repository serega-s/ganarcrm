from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('clients', views.ClientViewSet, basename='clients')
router.register('notes', views.NoteViewSet, basename='notes')

urlpatterns = [
    path('convert_lead_to_client/', views.convert_lead_to_client),
    path('clients/delete_client/<int:client_id>/',
         views.delete_client),
    path('', include(router.urls))
]
