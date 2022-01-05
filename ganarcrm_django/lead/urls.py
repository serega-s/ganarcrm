from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('leads', views.LeadViewSet, basename='leads')

urlpatterns = [
    path('leads/delete_lead/<int:lead_id>/', views.delete_lead),
    path('', include(router.urls))
]
