from django.contrib import admin
from django.urls import path
from api10 import views   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/get', views.StudentList.as_view()),
    path('studentapi/post', views.StudentCreate.as_view()),
    # path('studentapi/<int:pk>', views.StudentRetrieve.as_view()),# I have giving some id to retrieve single data
    # path('studentapi/<int:pk>/',views.StudentUpdate.as_view()),
    path('studentapi/<int:pk>',views.StudentDestroy.as_view())
    
]
