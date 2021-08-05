"""meusgames URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from games.api.urls import router as router_games
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from games.api.views import CategoriaViewSet, GameViewSet, RegisterView, UserDetailView, UserListView, UserMeView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router_games.urls)),
# https://medium.com/@hudsonbrendon/autentica%C3%A7%C3%A3o-com-jwt-no-django-rest-framework-45626936c276
    url(r'^login/', obtain_jwt_token),
    url(r'^refresh-token/', refresh_jwt_token),

    path('me/', UserMeView.as_view()),
    path('users/', UserListView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),
    path('register/', RegisterView.as_view(), name='auth_register'),
]
