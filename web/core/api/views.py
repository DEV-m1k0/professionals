import json
from rest_framework.generics import *
from rest_framework.response import Response
from .serializers import *
from models.models import *

# Create your views here.



class CabineRetriveAPIView(RetrieveAPIView):
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializers

    def get(self, request, name: str, *args, **kwargs):
        try:
            cabinet = Cabinet.objects.get(title=name)
            serializer = CabinetSerializers(cabinet)
            return Response(serializer.data)
        except:
            return Response()


class CabineListAPIView(ListAPIView):
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializers


class JobTitleListAPIView(ListAPIView):
    queryset = Position.objects.all()
    serializer_class = JobTitleSerializers


class JobTitleByNameAPIView(ListAPIView):
    queryset = Position.objects.all()
    serializer_class = JobTitleSerializers

    def get(self, request, name: str, *args, **kwargs):
        try:
            job_title = Position.objects.get(title=name)
            serializer = JobTitleSerializers(job_title)
            return Response(serializer.data)
        except:
            return Response()


class OrganizationListApiView(ListAPIView):
    serializer_class = OrgarizationsSerializer
    queryset = Organization.objects.all()


class OrganizationByNameListApiView(ListAPIView):
    serializer_class = OrgarizationsSerializer
    queryset = Organization.objects.all()

    def get(self, request, name: str, *args, **kwargs):
        try:
            organizaation = Organization.objects.get(title=name)
            serializer = OrgarizationsSerializer(organizaation)
            return Response(serializer.data)
        except:
            return Response()


class SubDivisionListApiView(ListAPIView):
    serializer_class = SubDivisionsSerializer
    queryset = Subdivision.objects.all()


class SubDivisionByNameListApiView(ListAPIView):
    serializer_class = SubDivisionsSerializer
    queryset = Subdivision.objects.all()


    def get(self, request, name: str, *args, **kwargs):
        try:
            sub_division = Subdivision.objects.get(title=name)
            serializer = SubDivisionsSerializer(sub_division)
            return Response(serializer.data)
        except: 
            return Response

class SubSubDivisionListApiView(ListAPIView):
    serializer_class = SubSubDivisionsSerializer
    queryset = SubSubDivision.objects.all()


class SubSubDivisionByNameListApiView(ListAPIView):
    serializer_class = SubSubDivisionsSerializer
    queryset = SubSubDivision.objects.all()

    def get(self, request, name: str, *args, **kwargs):
        try:
            sub_sub_division = SubSubDivision.objects.get(title=name)
            serializer = SubDivisionsSerializer(sub_sub_division)
            return Response(serializer.data)
        except: 
            return Response


class EmployeeListApiView(ListAPIView, CreateAPIView):
    serializer_class = EmployeesSerializer
    queryset = Employee.objects.all()


class EmployeeSearchByNameApiView(ListAPIView):
    serializer_class = EmployeesSerializer
    queryset = Employee.objects.all()

    def get(self, request, name: str, *args, **kwargs):
        try:
            employee = Employee.objects.get(username=name)
            serializer = EmployeesSerializer(employee)
            return Response(serializer.data)
        except:
            return Response()

class EmployeeSearchByDepartmentApiView(ListAPIView):
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