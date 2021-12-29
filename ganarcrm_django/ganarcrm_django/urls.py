from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),

    path('api/v1/token/', TokenObtainPairView.as_view()),
    path('api/v1/token/refresh/', TokenRefreshView.as_view()),

    path('api/v1/', include('lead.urls')),
    path('api/v1/', include('team.urls')),
    path('api/v1/', include('client.urls')),
]
