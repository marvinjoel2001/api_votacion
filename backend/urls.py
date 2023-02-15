from rest_framework import routers
from .api import UserViewSet, JuradoViewSet, OrganitationViewSet, CalificationViewSet, CategoryViewSet, VoteViewSet

router = routers.DefaultRouter()

router.register('api/user', UserViewSet, 'users')
router.register('api/jurado', JuradoViewSet, 'jurados')
router.register('api/category', CategoryViewSet, 'category')
router.register('api/organitation', OrganitationViewSet, 'organitation')
router.register('api/calification', CalificationViewSet, 'calification')
router.register('api/vote', VoteViewSet, 'vote')
urlpatterns = router.urls
