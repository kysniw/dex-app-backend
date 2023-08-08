from django.urls import path, include

from rest_framework.routers import DefaultRouter

from window_sill import views

router = DefaultRouter()
# router.register('manage_sill', views.WindowSillCreateView)
router.register('get_sill', views.WindowSillView)

app_name = 'window_sill'

urlpatterns = [
    path('', include(router.urls)),
]
