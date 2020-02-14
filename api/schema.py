import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Patient
from accounts.models import Facility


class PatientNode(DjangoObjectType):
    class Meta:
        model = Patient
        filter_fields = {
            "full_name": ["exact", "icontains"],
            "uid": ["exact"],
            "facility__facility_name": ["exact", "icontains"],
        }
        interfaces = (relay.Node,)

    @classmethod
    def get_queryset(cls, queryset, info):
        if not info.context.user.is_authenticated:
            return Patient.objects.none()
        else:
            return Patient.objects.filter(facility=info.context.user.facility)


class Query(graphene.ObjectType):
    patient = relay.Node.Field(PatientNode)
    my_patients = DjangoFilterConnectionField(PatientNode)
