from rest_framework.serializers import ModelSerializer
from models.models import *

class EventSerializers(ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

class SkipDataSerializers(ModelSerializer):
    class Meta:
        model = CalendarSkip
        fields = ["date_since", "date_until"]
        
class VacationDateSerializers(ModelSerializer):
    class Meta:
        model = CalendarVacation
        fields = ["date_since", "date_until"]

class EventDataSerializers(ModelSerializer):
    class Meta:
        model = Event
        fields = ["date_since", "date_until"]
        

class CabinetSerializers(ModelSerializer):
    class Meta:
        model = Cabinet
        fields = "__all__"


class JobTitleSerializers(ModelSerializer):
    class Meta:
        model = Position
        fields = "__all__"


class OrgarizationsSerializer(ModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"


class SubDivisionsSerializer(ModelSerializer):
    class Meta:
        model = Subdivision
        fields = "__all__"


class SubSubDivisionsSerializer(ModelSerializer):
    class Meta:
        model = SubSubDivision
        fields = "__all__"



class EmployeesSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"