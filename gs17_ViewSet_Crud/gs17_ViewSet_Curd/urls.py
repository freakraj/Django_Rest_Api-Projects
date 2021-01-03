from django.contrib import admin
from django.urls import path,include
from api10 import views
from rest_framework.routers import DefaultRouter

# Create Router Object 
router = DefaultRouter()


# Register StudentViewSet with Router (with multiple methods )
router.register('studentapi',views.StudentViewSet, basename='student')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
