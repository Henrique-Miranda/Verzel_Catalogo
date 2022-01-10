from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views as authview
from api import views as api_views

router = routers.DefaultRouter()
router.register(r'lessons', api_views.LessonViewSet)
router.register(r'modules', api_views.ModuleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    # https://www.django-rest-framework.org/api-guide/authentication/ Generate token if ot exists
    path('api-token-auth/', authview.obtain_auth_token, name='api-token-auth'),
    path('admin/', admin.site.urls),

]