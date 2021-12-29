from django.db.models import base
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('teams', views.TeamViewSet, basename='teams')

urlpatterns = [
    path('teams/member/<int:pk>/', views.UserDetail.as_view(), name='userdetail'),
    path('teams/get_my_team/', views.get_my_team),
    path('teams/add_member/', views.add_member),
    path('teams/upgrade_plan/', views.upgrade_plan),
    path('teams/cancel_plan/', views.cancel_plan),
    path('stripe/get_stipe_pub_key/',
         views.get_stripe_pub_key),
    path('stripe/create_checkout_session/',
         views.create_checkout_session_and_upgrade_plan),
    path('stripe/webhook/', views.stripe_webhook),
    path('stripe/check_session/', views.check_session),

    path('', include(router.urls)),
]
