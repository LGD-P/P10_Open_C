from django.urls import path, include
from rest_framework_nested import routers


from app.views import (ProjectViewset, ContributorViewset,
                       IssuetViewset, CommentViewset)

router = routers.DefaultRouter()

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
    path('', include(router.urls)),
    path('', include(contributor_nested_router.urls)),
    path('', include(issue_nested_router.urls)),
    path('', include(comment_nested_router.urls)),
]
