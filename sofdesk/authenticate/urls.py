from django.urls import path, include
from rest_framework_nested import routers


from authenticate.views import UserViewset

router = routers.DefaultRouter()

router.register('user', UserViewset, basename='user')


urlpatterns = [

    path('', include(router.urls)),

]
