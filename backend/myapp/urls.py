from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .view_sets import PokemonViewSet, HelpRequestViewSet, UserCreate
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http import HttpResponseRedirect

router = DefaultRouter()
router.register(r'pokemon', PokemonViewSet)
router.register(r'help-requests', HelpRequestViewSet)


def redirect_to_login(request):
    return HttpResponseRedirect('/api/token/')

urlpatterns = [
    path('', redirect_to_login, name='home'),   
    path('api/register/', UserCreate.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
]