from rest_framework.generics import ListAPIView
from .serializers import (
    OrgarizationsSerializer, SubDivisionsSerializer, SubSubDivisionsSerializer,
    EmployeesSerializer
    )
from models.models import (
    Organization, Subdivision, SubSubDivision,
    Employee
    )

# Create your views here.


class OrganizationListApiView(ListAPIView):
    serializer_class = OrgarizationsSerializer
    queryset = Organization.objects.all()



class SubDivisionListApiView(ListAPIView):
    serializer_class = SubDivisionsSerializer
    queryset = Subdivision.objects.all()



class SubSubDivisionListApiView(ListAPIView):
    serializer_class = SubSubDivisionsSerializer
    queryset = SubSubDivision.objects.all()


class EmployeeListApiView(ListAPIView):
    serializer_class = EmployeesSerializer
    queryset = Employee.objects.all()