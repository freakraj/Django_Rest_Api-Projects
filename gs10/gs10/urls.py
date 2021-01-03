from django.contrib import admin
from django.urls import path
from api10 import views   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.student_api)
]
