from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

from api.views import (CommentViewSet, ReviewViewSet, TitelViewSet,
                       UserViewSet, get_jwt_token, send_code)
from api.views.category_genre import CategoryOrGenreViewSet

router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router_v1.register('genres', CategoryOrGenreViewSet, basename='genres')
router_v1.register('categories', CategoryOrGenreViewSet, basename='categories')
router_v1.register('titles', TitelViewSet)

urlpatterns = [
    path('v1/auth/email/', send_code),
    path('v1/auth/token/', get_jwt_token, name='get_jwt_token'),
    path('v1/', include(router_v1.urls)),
]
