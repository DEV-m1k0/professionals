import json
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
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


class EmployeeSearchApiView(ListAPIView):
    serializer_class = EmployeesSerializer
    queryset = Employee.objects.all()

    def get(self, request, department: str, *args, **kwargs):
        try:
            organization = Organization.objects.get(title=department)
            serializer = EmployeesSerializer(Employee.objects.filter(organization=organization), many=True)
            return Response(serializer.data)
        except:
            pass
        try:
            sub_division = Subdivision.objects.get(title=department)
            serializer = EmployeesSerializer(Employee.objects.filter(subdivision=sub_division), many=True)
            return Response(serializer.data)
        except:
            pass
        try:
            sub_sub_division = SubSubDivision.objects.get(title=department)
            serializer = EmployeesSerializer(Employee.objects.filter(sub_sub_division=sub_sub_division), many=True)
            return Response(serializer.data)
        except:
            pass
        return Response()