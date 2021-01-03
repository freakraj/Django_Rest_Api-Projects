from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets # isse modelviewset bhi a jayega

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
