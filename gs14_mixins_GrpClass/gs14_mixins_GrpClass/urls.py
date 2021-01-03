from django.contrib import admin
from django.urls import path
from api10 import views   

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('studentapi/', views.LCStudentAPI.as_view()),
    # THIS URL FOR LIST AND CREATE 
   
    path('studentapi/<int:pk>/',views.RUDStudentAPI.as_view())
    # THIS URL FOR RETRIEVE UPDATE AND DESTROYE
    
]
