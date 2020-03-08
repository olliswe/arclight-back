import graphene
from graphene_django.types import DjangoObjectType
from .models import Patient
from graphene_django_extras.fields import DjangoFilterListField


class Patient(DjangoObjectType):
    age = graphene.String(source="age")

    class Meta:
        model = Patient
        filter_fields = {
            "full_name": ["exact", "icontains"],
            "facility__facility_name": ["exact", "icontains"],
        }

    # @classmethod
    # def get_queryset(cls, queryset, info):
    #     if not info.context.user.is_authenticated:
    #         return Patient.objects.none()
    #     else:
    #         return Patient.objects.filter(facility=info.context.user.facility)


class Query(graphene.ObjectType):
    patient = graphene.Field(Patient, patient_id=graphene.String())
    my_patients = DjangoFilterListField(Patient)

    def resolve_patient(self, info, patient_id):
        return Patient.objects.get(pk=patient_id)

    def resolve_my_patients(self, info, **kwargs):
        return Patient.objects.filter(facility=info.context.user.facility)
