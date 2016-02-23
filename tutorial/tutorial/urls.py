from django.conf.urls import url, include
from rest_framework import routers
from snippets import views as snippets_views
from vacancy import views as vacancy_views

router = routers.DefaultRouter()
router.register(r'users', snippets_views.UserViewSet)
router.register(r'groups', snippets_views.GroupViewSet)

router.register(r'joks', vacancy_views.FunnyJokesViewSet)
router.register(r'vote_up', vacancy_views.VoteUpViewSet)
router.register(r'description', vacancy_views.DescriptionViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]