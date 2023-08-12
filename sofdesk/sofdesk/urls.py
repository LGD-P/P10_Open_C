
from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from authenticate.views import UserViewset
from app.views import (ProjectViewset, ContributorViewset,
                       IssuetViewset, CommentViewset)


router = routers.DefaultRouter()

router.register('user', UserViewset, basename='user')
router.register('project', ProjectViewset, basename='project')
router.register('contributor', ContributorViewset, basename='contributor')
router.register('issue', IssuetViewset, basename='issue')
router.register('comment', CommentViewset, basename='comment')


# Router pour les Contirbuteur
contributor_nested_router = routers.NestedDefaultRouter(
    router, 'project', lookup='project')
contributor_nested_router.register(
    'contributor', ContributorViewset, basename="contributor")

# Router pour les Issues remontant vers les Project
issue_nested_router = routers.NestedDefaultRouter(
    router, 'project', lookup='project')
issue_nested_router.register('issue', IssuetViewset, basename='issue')

# Router pour les Commentaires remontant vers les Issues
comment_nested_router = routers.NestedDefaultRouter(
    issue_nested_router, 'issue', lookup='issue')
comment_nested_router.register('comment', CommentViewset, basename='comment')


urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),


    path('api/', include(contributor_nested_router.urls)),
    path('api/', include(issue_nested_router.urls)),
    path('api/', include(comment_nested_router.urls)),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),



]
