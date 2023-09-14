from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
# router.register('manage_sill', views.WindowSillCreateView)
router.register('', views.OrderViewset)

app_name = 'order'

urlpatterns = [
    path('', include(router.urls)),
]