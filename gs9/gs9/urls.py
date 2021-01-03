from django.contrib import admin
from django.urls import path
from api9 import views   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.hello_word)
]
