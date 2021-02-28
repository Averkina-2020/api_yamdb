from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import UserViewSet, get_jwt_token, send_code

router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet)


urlpatterns = [    
    path('v1/auth/email/', send_code, name='send_code'),
    path('v1/auth/token/', get_jwt_token, name='get_jwt_token'),
    path('v1/', include(router_v1.urls)),
]
